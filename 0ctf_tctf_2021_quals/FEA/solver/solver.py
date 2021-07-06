from pwn import *
import base64
import subprocess
import binascii
from unicorn import *
from unicorn.x86_const import *
# from tea import *
from IDEA_oneround import encipher, decipher
import time
import string
from hashlib import sha256
import gmpy2

#p = remote("127.0.0.1", "30212")
#p = remote("111.186.58.164", "30212")
p = remote("13.213.48.68", "30212")

def proof_of_work():
    p.recvuntil(b"sha256(XXXX+")
    endd = p.recv(16)
    print(endd)
    p.recvuntil(b"== ")
    hexdigest = p.recv(64).decode()
    print(hexdigest)
    charset = string.ascii_letters + string.digits
    for a0 in charset:
        for a1 in charset:
            for a2 in charset:
                for a3 in charset:
                    tmpp = (a0 + a1 + a2 + a3).encode()
                    s = tmpp + endd
                    if sha256(s).hexdigest() == hexdigest:
                        print(f"PoW: {tmpp}")
                        p.send(tmpp)
                        return
    assert "PoW Error"
    exit(0)

proof_of_work()

ticks = time.time()

for _ in range(3):
    p.recvuntil("Here is your challenge:\n\n")
    b64 = p.recvline()[:-1]
    # print(b64)
    binary = base64.b64decode(b64)
    with open("./tmpfile", "wb") as f:
        f.write(binary)

    result = subprocess.check_output(["objdump", "-d", "./tmpfile"])
    ll = result.splitlines()
    for idx, l in enumerate(ll):
        if b"6060d0" in l:
            dis_ = ll[idx+2]
    lz_len = int(dis_[dis_.index(b"$")+1:dis_.index(b",")], 16)

    with open("sc.compressed", "wb") as f:
        f.write(binary[0x60d0:0x60d0+lz_len])
    # ./unpacker sc.compressed sc.decompressed
    subprocess.check_output(["./unpacker", "sc.compressed", "sc.decompressed"])
    with open("sc.decompressed", "rb") as f:
        sc = f.read()

    # pattern = [
    #     binascii.unhexlify(b"EB 03 88 C3 BA E8 F9 FF FF FF".replace(b" ", b"")),
    #     binascii.unhexlify(b"E8 04 00 00 00 77 EB 07 88 48 83 04 24 01 C3".replace(b" ", b"")),
    # ]
    # for pat in pattern:
    #     sc = sc.replace(pat, b"\x90"*len(pat))
    # with open("sc", "wb") as f:
    #     f.write(sc)


    def hook_intr(uc, intno, data):
        # print(intno)
        # uc.emu_stop()
        res = u32(uc.mem_read(DEADBUF, 4)) ^ 0xdeadbeef
        uc.mem_write(DEADBUF, p32(res))
        pass

    def hook_code64(uc, address, size, user_data):
        # print(">>> Tracing instruction at 0x%x, instruction size = 0x%x" %(address, size))
        rip = uc.reg_read(UC_X86_REG_RIP)
        print(">>> RIP is 0x%x" %rip)

    def hook_mem_invalid(uc, access, address, size, value, user_data):
        rip = uc.reg_read(UC_X86_REG_RIP)
        print(">>> RIP is 0x%x" %rip)
        if access == UC_HOOK_MEM_READ_UNMAPPED:
            print(">>> Missing memory is being READ at 0x%x, data size = %u, data value = 0x%x" \
                    %(address, size, value))
            return False
        else:
            print(">>> Missing memory is being WRITE at 0x%x, data size = %u, data value = 0x%x" \
                    %(address, size, value))
            # return False to indicate we want to stop emulation
            return False
    
    CODE = 0x1000000
    STACK = 0x2000000
    DATA = 0x3000000
    DEADBUF = 0xdead0000

    mu = Uc(UC_ARCH_X86, UC_MODE_64)
    mu.mem_map(DEADBUF, 2 * 1024 * 1024)
    mu.mem_map(CODE, 2 * 1024 * 1024)
    mu.mem_write(CODE, sc)
    mu.mem_map(STACK, 4 * 1024 * 1024)
    mu.reg_write(UC_X86_REG_RSP, STACK + 0x400000-0x100)
    mu.mem_map(DATA, 2 * 1024 * 1024)
    mu.reg_write(UC_X86_REG_RDI, DATA)
    mu.hook_add(UC_HOOK_INTR, hook_intr)
    mu.hook_add(UC_HOOK_MEM_READ_UNMAPPED | UC_HOOK_MEM_WRITE_UNMAPPED, hook_mem_invalid)
    # mu.hook_add(UC_HOOK_CODE, hook_code64)

    # func_end = sc.index(b"\xC9\xC3")
    # func_end = sc.index(b"\xC3\x55")
    func_end = sc.index(b"\xC3\x55\x48\x89\xE5")
    mu.emu_start(CODE, CODE + func_end)
    print(f"func_end: {hex(func_end)}")

    res = mu.mem_read(DATA, 8)
    # print(res)
    v = [u32(res[0:4]), u32(res[4:8])]
    print(f"ciphertext(v): {v}")

    # key = [2, 2, 3, 4]
    rk = [7,6,5,4,3,2]
    irk = [int(gmpy2.invert(rk[0], 0x10001)), 0x10000 - rk[1], 0x10000 - rk[2], int(gmpy2.invert(rk[3], 0x10001)),
           rk[4], rk[5]]
    ans = decipher(v, irk)
    print(f"input: {ans}")
    payload = p32(ans[0]) + p32(ans[1])
    p.send(payload)

print(p.recvall())
print(f"Used {time.time()-ticks}s")

# p.interactive()
