import random

MASK=0xFFFFFFFF
NUM_BITS=8


def add(a, b):
    return (a+b) & MASK
def sub(a, b):
    return (a-b) & MASK
def mul(a, b):
    return (a*b) & MASK
def div(a, b):
    return (a//b) & MASK
def mod(a, b):
    return (a%b) & MASK
def ror(a, b):
    return ((((a) & MASK) >> (b%NUM_BITS)) | (((a) << (NUM_BITS - (b%NUM_BITS))) & MASK))
def rol(a, b):
    return ((((a) << (b%NUM_BITS)) & MASK) | (((a) & MASK) >> (NUM_BITS - (b%NUM_BITS))))
def bit_xor(a, b):
    return a ^ b
def bit_and(a, b):
    return a & b
def bit_or(a, b):
    return a | b

def JUNK11(a, b):
    return a
def JUNK22(a, b):
    return a
def INT3_ANTI(a, b):
    return a ^ 0xdeadbeef

obf_h_append = ""

templ_junk11 = """#define JUNK11_%d(idx) __asm__ __volatile__ (  \\
"jmp jlabel"#idx"\\n\\t" \\
%s"jlabel_"#idx" :\\n\\t" \\
"ret\\n\\t" \\
%s"jlabel"#idx" :\\n\\t" \\
"call jlabel_"#idx"\\n\\t"  \\
);\n\n"""

def JUNK11_RANDOM(a, b, f=0):
    if f == 0:
        return a
    else:
        idx = random.randint(0x100000, 0x1000000)
        s1 = ""
        for _ in range(random.randint(1, 8)):
            s1 += """".byte %s\\n\\t" \\\n""" % hex(random.randint(0, 0xff))
        s2 = ""
        for _ in range(random.randint(1, 8)):
            s2 += """".byte %s\\n\\t" \\\n""" % hex(random.randint(0, 0xff))
        global obf_h_append
        obf_h_append += templ_junk11 % (idx, s1, s2)
        return "JUNK11_%d(%d)" % (idx, idx)

templ_junk22 = """#define JUNK22_%d(idx) __asm__ __volatile__ (  \\
"call next1_junk2_"#idx"\\n\\t"    \\
%s"jmp next_junk2_"#idx"\\n\\t"      \\
%s"next1_junk2_"#idx":\\n\\t"        \\
"addq $1, (%%rsp)\\n\\t" \\
"ret\\n\\t"                       \\
"next_junk2_"#idx":\\n\\t"         \\
);\n\n"""
    
def JUNK22_RANDOM(a, b, f=0):
    if f == 0:
        return a
    else:
        idx = random.randint(0x100000, 0x1000000)
        s1 = ""
        s1 += """".byte %s\\n\\t" \\\n""" % hex(random.randint(0, 0xff))
        s2 = ""
        for _ in range(random.randint(1, 8)):
            s2 += """".byte %s\\n\\t" \\\n""" % hex(random.randint(0, 0xff))
        global obf_h_append
        obf_h_append += templ_junk22 % (idx, s1, s2)
        return "JUNK22_%d(%d)" % (idx, idx)


op_list = [add, sub, mul, div, mod, ror, rol, bit_xor, bit_and, bit_or, JUNK11, JUNK22, INT3_ANTI, 
    JUNK11_RANDOM, JUNK22_RANDOM]

marco = [JUNK11, JUNK22, INT3_ANTI]
int3 = [INT3_ANTI]
junk_random = [JUNK11_RANDOM, JUNK22_RANDOM]

def create_obf_h():
    with open("obf.h.tmp", "r") as f:
        obf_h = f.read()
    with open("obf.h", "w") as f:
        f.write(obf_h[:obf_h.index("\n#endif")])
        f.write(obf_h_append)
        f.write("\n#endif")

