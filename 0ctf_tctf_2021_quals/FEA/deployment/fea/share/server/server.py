#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import socketserver
# import numpy
import os, signal
import string, binascii
from hashlib import sha256
import base64
import subprocess
# from tea import decipher
from op import *
import sys
# from tea import *
from IDEA_oneround import encipher, decipher
import gmpy2

# from Crypto.Random import random, atfork
import random

from secret import FLAG

class Task():
    _phase = 0

    # def _recvall(self):
    #     BUFF_SIZE = 2048
    #     data = b''
    #     while True:
    #         part = self.request.recv(BUFF_SIZE)
    #         data += part
    #         if len(part) < BUFF_SIZE:
    #             break
    #     return data.strip()

    # def send(self, msg, newline=True):
    #     try:
    #         if newline:
    #             msg += b'\n'
    #         self.request.sendall(msg)
    #     except:
    #         pass

    # def recv(self, prompt=b''):
    #     self.send(prompt, newline=False)
    #     return self._recvall()

    def send(self, msg, newline=True):
        # if newline:
        # print(msg)
        sys.stdout.write(msg)
        sys.stdout.write(b"\n")
        sys.stdout.flush()
        # else:
            # print(msg, end='')

    def recv(self, len, prompt=b''):
        if prompt != b'':
            sys.stdout.write(prompt)
        return sys.stdin.read(len)
    
    def print_dbg(self, msg):
        sys.stderr.write((msg+"\n").encode())

    def proof_of_work(self):
        signal.alarm(30)
        proof = ''.join(
            [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        )
        # proof = "1"*20
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(str.encode("sha256(XXXX+%s) == %s" % (proof[4:], _hexdigest)))
        self.send("Give me XXXX: ")
        x = self.recv(4)

        if len(x) != 4 or sha256(x + proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True

    def timeout_handler(self, signum, frame):
        self.send(b"\n\nSorry, time out.\n")
        raise TimeoutError

    def gen_chall_ans(self):
        # key = [2, 2, 3, 4]
        rk = [7,6,5,4,3,2]
        irk = [int(gmpy2.invert(rk[0], 0x10001)), 0x10000 - rk[1], 0x10000 - rk[2], int(gmpy2.invert(rk[3], 0x10001)),
           rk[4], rk[5]]
        # v = [0x1300f065, 0xca437c68]
        v = []
        v.append(random.randint(0, 0x100000000-1))
        v.append(random.randint(0, 0x100000000-1))
        # v = [0x41414141, 0x41414141]
        ans = encipher(v, rk)
        # ans = decipher(v, irk)

        self.print_dbg(("ciphertext = [0x%x, 0x%x], v = [0x%x, 0x%x]" % (v[0], v[1], ans[0], ans[1])).encode())
        # print("v = [0x%x, 0x%x], ans = [0x%x, 0x%x]" % (v[0], v[1], ans[0], ans[1]))

        return ans

    def gen_obf_func(self, target):
        res = 0
        code = []
        OP_SIZE = len(op_list)

        for _ in range(0x1000):
            bitsize = random.randint(4, 7)
            rr = random.randint(2 << (bitsize), (2 << (bitsize + 1)) - 1)
            op_code = random.randint(0, OP_SIZE-1)

            res = op_list[op_code](res, rr)
            if op_list[op_code] in junk_random:
                code.append(op_list[op_code](res, rr, 1))
            elif op_list[op_code] not in marco:
                code.append("res = %s(res, %d);" % (op_list[op_code].__name__, rr))
            elif op_list[op_code] not in int3:
                code.append("%s(%d)" % (op_list[op_code].__name__, random.randint(0x100000, 0x1000000)))
            else:
                code.append("%s" % (op_list[op_code].__name__))

        create_obf_h()

        code.append("v[0] = res + %d;" % ((target[0] - res) & MASK))
        code.append("v[1] = res + %d;" % ((target[1] - res) & MASK))

        with open("target_obf.h", "w") as f:
            f.write("""#include "op.h"
#include "obf.h"
#include <stdint.h>
void obf_func(uint32_t *v) {uint32_t res = v[0]^v[1];\n
register uint32_t *ptr = 0xdead0000;
""")
            f.write(("\n".join(code)))
            f.write("""return;
}""")

    def assemble_file(self):

        target = self.gen_chall_ans()
        self.gen_obf_func(target)

        filename = "./" + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        # print("./packer %s %s_packed" % (filename, filename))
        os.system("gcc -O0 -fno-stack-protector checker.c -o {:s}".format(filename))
        os.system("./packer %s %s_packed" % (filename, filename))
        return filename+"_packed"

    def encode_file_to_player(self, filename):
        with open(filename, "rb") as f:
            rawelf = f.read()
            b64elf = base64.b64encode(rawelf)
        self.send(b'Here is your challenge:\n')
        self.send(b64elf)
        self.send(b'\n')

    def check(self, filename):
        try:
            result = subprocess.check_output([filename])
            print(result)
            if 'Right' in result:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
        finally:
            pass
            subprocess.check_output(['rm', filename])
            subprocess.check_output(['rm', filename.replace("_packed", "")])

    def handle(self):
        if not self.proof_of_work():
            self.send("please pof first")
            exit(0)
        
        for _ in range(0, 3):
            self.send("[%d/%d]" % (_+1, 3))
            self._phase = _
            
            filename = self.assemble_file()
            self.print_dbg(filename)
            self.encode_file_to_player(filename)
            self.send("Plz beat me in 10 seconds X3 :)")
            signal.alarm(10)
            res = self.check(filename)
            if res != True:
                self.send(b'Try again~')
                # self.request.close()
                return
            signal.alarm(0)

        self.send(b'Nice gob. Here is your flag:')
        self.send(FLAG.encode())
        # self.request.close()

        # except:
        # pass



if __name__ == "__main__":
    task = Task()
    task.handle()
