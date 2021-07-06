// gcc ./checker.c -O0 -fno-stack-protector -o checker




#include <unistd.h>
#include <sys/syscall.h>   /* For SYS_xxx definitions */
#include <stdint.h>

#define __TARGET_OBF
#ifdef __TARGET_OBF
#include "target_obf.h"
#endif

#define __ASM_OBF
#ifdef __ASM_OBF
#include "obf.h"
#endif

// #define __INT_ANTIDEBUG

__attribute__((noinline))
void my_syscall(int a, ...) {
    #ifdef __INT_ANTIDEBUG
    INT3_ANTI_ONLY
    #endif
    #ifdef __ASM_OBF
    JUNK22(5)JUNK11(5)
    #endif
    __asm__ __volatile__ (
        "movq %rdi, %rax\n\t"       /* Syscall number -> rax.  */
        "movq %rsi, %rdi\n\t"
        "movq %rdx, %rsi\n\t"
        "movq %rcx, %rdx\n\t"
        "syscall\n\t"
        );
    return;
}

//加密函数
// void tea_encrypt(uint32_t *v, uint32_t *k)
// {
//     uint32_t v0 = v[0], v1 = v[1], sum = 0, i;           /* set up */
//     uint32_t delta = 0x9e3779b9;                         /* a key schedule constant */
//     uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3]; /* cache key */
//     for (i = 0; i < 32; i++)
//     { /* basic cycle start */
//         sum += delta;
//         v0 += ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
//         v1 += ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);
//     } /* end cycle */
//     v[0] = v0;
//     v[1] = v1;
// }

//解密函数
// void tea_decrypt(uint32_t *v, uint32_t *k)
// {
//     my_syscall(SYS_gettimeofday, 0, 0, 0);      // 叶子函数 没有sub rsp xxx， v0 v1正好在rsp，call后被覆盖

//     #ifdef __ASM_OBF
//     JUNK22(6)
//     #ifdef __INT_ANTIDEBUG
//     INT3_ANTI_ONLY
//     #endif
//     JUNK11(6)
//     #endif

//     uint32_t v0 = v[0], v1 = v[1], sum = 0xC6EF3720, i; /* set up */ // uint32_t sum = delta << 5;                      //32轮运算，所以是2的5次方；16轮运算，所以是2的4次方；8轮运算，所以是2的3次方
//     uint32_t delta = 0x9e3779b9;                                     /* a key schedule constant */
//     uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];             /* cache key */
//     for (i = 0; i < 32; i++)
//     { /* basic cycle start */
//         #ifdef __ASM_OBF
//         JUNK22(7)
//         #endif
//         v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);
//         v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
//         #ifdef __ASM_OBF
//         JUNK11(7)
//         #endif
//         sum -= delta;
//     } /* end cycle */

//     #ifdef __ASM_OBF
//     JUNK22(8)                    // 叶子函数 没有sub rsp xxx， v0 v1正好在rsp，call后被覆盖
//     JUNK11(8)
//     #endif

//     v[0] = v0;
//     v[1] = v1;
// }



#define idea_mul(r,a,b,ul) \
ul=(unsigned long)a*b; \
if (ul != 0) \
	{ \
	r=(ul&0xffff)-(ul>>16); \
	r-=((r)>>16); \
	} \
else \
	r=(-(int)a-b+1); /* assuming a or b is 0 and in range */

void test();
void encrypt(uint32_t *d)
{
    // register IDEA_INT *p;
    register uint32_t x1,x2,x3,x4,t0,t1,ul;

    // my_syscall(SYS_gettimeofday, 0, 0, 0);      // 叶子函数 没有sub rsp xxx， v0 v1正好在rsp，call后被覆盖
    test();

    x2=d[0];
    x1=(x2>>16);
    x4=d[1];
    x3=(x4>>16);

    // p= &(key->data[0][0]);

    x1&=0xffff;
    // idea_mul(x1,x1,*p,ul); p++;
    idea_mul(x1,x1,7,ul);
    // x2+= *(p++);
    x2+= 6;
    // x3+= *(p++);
    x3+= 5;
    x4&=0xffff;
    // idea_mul(x4,x4,*p,ul); p++;
    idea_mul(x4,x4,4,ul);
    t0=(x1^x3)&0xffff;
    // idea_mul(t0,t0,*p,ul); p++;
    idea_mul(t0,t0,3,ul);
    t1=(t0+(x2^x4))&0xffff;
    // idea_mul(t1,t1,*p,ul); p++;
    idea_mul(t1,t1,2,ul);
    t0+=t1;
    x1^=t1;
    x4^=t0;
    ul=x2^t0; /* do the swap to x3 */
    x2=x3^t1;
    x3=ul;

    d[0]=(x2&0xffff)|((x1&0xffff)<<16);
    d[1]=(x4&0xffff)|((x3&0xffff)<<16);
}

// #define SET_WELCOME(x) x[0]='?',x[1]='>',x[2]='\n',x[3]=0
#define SET_RIGHT(x) x[0]='R',x[1]='i',x[2]='g',x[3]='h',x[4]='t',x[5]='!',x[6]='\n',x[7]=0
#define SET_WRONG(x) x[0]='W',x[1]='r',x[2]='o',x[3]='n',x[4]='g',x[5]='!',x[6]='\n',x[7]=0

int main()
{
    #ifdef __INT_ANTIDEBUG
    INT3_ANTI_ONLY
    #endif

    // uint32_t k[4] = {2, 2, 3, 4};
    uint32_t vv[2] = {0, 0};
    char str[10];

    // SET_WELCOME(str);
    // my_syscall(SYS_write, 1, str, 4);

    #ifdef __ASM_OBF
    JUNK11(1)JUNK22(1)
    #endif
    #ifdef __INT_ANTIDEBUG
    INT3_ANTI_ONLY
    #endif
    
    my_syscall(SYS_read, 0, vv, 8);
    
    // tea_decrypt(vv, k);
    encrypt(vv);

    uint32_t target[2] = {
        // 1, 2
        // 0x1300f065, 0xca437c68              // "43218765"
        0, 0
        };
    
    #ifdef __ASM_OBF
    JUNK11(2)
    #endif

    #ifdef __TARGET_OBF
    obf_func(target);
    #endif
    
    #ifdef __ASM_OBF
    JUNK22(2)
    #endif

    if (vv[0] == target[0] && vv[1] == target[1])
    {
        
        #ifdef __ASM_OBF
        JUNK22(3)JUNK11(3)
        #endif

        // puts("Right!");
        SET_RIGHT(str);
        my_syscall(SYS_write, 1, str, 8);
        return 0;
    }
    else
    {
        #ifdef __ASM_OBF
        JUNK22(4)JUNK11(4)
        #endif

        // puts("Wrong!");
        SET_WRONG(str);
        my_syscall(SYS_write, 1, str, 8);
        return -1;
    }
}

void test() {}