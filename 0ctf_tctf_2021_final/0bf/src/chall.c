//
// Created by G6 on 2021-09-17.
//

#include "stdint.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "mba_obf.h"

#define MASK 0xffffffff
#define BITSHIFT 32


// #define idea_mul(num, r,a,b,ul) \
// ul=(unsigned long long)a*b; \
// if (ul != 0) \
// 	{ \
// 	r=(ul&MASK)-(ul>>BITSHIFT); \
// 	r-=((r)>>BITSHIFT); \
// 	} \
// else \
//     r=(uint32_t)(ADD2((-(long long int)a), (-b+1), num)); /* assuming a or b is 0 and in range */
// 	// r=(uint32_t)(-(long long int)a-b+1); /* assuming a or b is 0 and in range */

#define idea_mul(num, r,a,b,ul) \
ul=(unsigned long long)a*b; \
if (ul != 0) \
	{ \
	r = ADD5((ul&MASK), (~(ul>>BITSHIFT)+1), ul); \
    r = ADD6(r, ((~((r)>>BITSHIFT)) + 1), b); \
	} \
else \
    r=(uint32_t)(ADD3((-(long long int)a), (-b+1), ul)); /* assuming a or b is 0 and in range */


#define IN(num, r, x0, x1, t0, t1, ul, k1, k2, k3, k4) \
   idea_mul(num, t0, (uint32_t)(XOR4(x0, x1, k1)), k1, ul) \
   t1 = (uint32_t)(XOR3(t0, k2)); \
   idea_mul(num, t0,t0,k3,ul); \
   t1=ADD2(t0,t1, num)&MASK; \
   idea_mul(num, t1,t1,k4,ul); \
   t0=ADD4(t0,t1, obfvar2)&MASK; \
   r = (uint32_t)(XOR5(t0,t1, RAND_0_##num));

// #define IN(r, x0, x1, t0, t1, ul, k1, k2, k3, k4) \
//     idea_mul(t0, (uint32_t)(x0^x1), k1, ul) \
//     t1 = (uint32_t)(t0^k2); \
//     idea_mul(t0,t0,k3,ul); \
//     t1=(t0+t1)&MASK; \
//     idea_mul(t1,t1,k4,ul); \
//     t0=(t0+t1)&MASK; \
//     r = (uint32_t)(t0^t1);

//#define ROUNDDD(x0, x1, t0, t1, ul, tmp, k1, k2, k3, k4, k5, k6) \
//    x0 = x0 + k1; \
//    idea_mul(x1, x1, k2, ul); \
//    x0 = x0 & MASK; \
//    x1 = x1 & MASK; \
//    IN(tmp, x0, x1, t0, t1, ul, k3, k4, k5, k6) \
//    x0 ^= tmp; \
//    x1 ^= tmp;

#define ROUNDDD(num, x0, x1, t0, t1, ul, tmp, k1, k2, k3, k4, k5, k6) \
    x0 = ADD1(x0, k1, num); \
    idea_mul(num, x1, x1, k2, ul); \
    x0 = x0 & MASK; \
    x1 = x1 & MASK; \
    IN(num, tmp, x0, x1, t0, t1, ul, k3, k4, k5, k6) \
    x0 = XOR1(x0, tmp, t1); \
    x1 = XOR2(x1, tmp, t0);

#define ROUND 10

void encrypt(uint32_t *d) {
    uint64_t obfvar1, obfvar2;
    register uint64_t x0, x1, t0, t1, ul, tmp;
    x0 = d[0];
    x1 = d[1];


    // uint32_t *p = keys;
    // for (int _=0; _<ROUND; _++) {
    //     uint64_t k1=*p++, k2=*p++, k3=*p++, k4=*p++, k5=*p++, k6=*p++;
    //     // x0 = ADD1(x0, k1);
    //     // // x0 = x0+ k1;
    //     // idea_mul(x1, x1, k2, ul);
    //     // x0 = x0 & MASK;
    //     // x1 = x1 & MASK;
    //     // IN(tmp, x0, x1, t0, t1, ul, k3, k4, k5, k6)
    //     // x0 ^= tmp;
    //     // x1 ^= tmp;
    //    ROUNDDD(x0, x1, t0, t1, ul, tmp, k1,k2,k3,k4,k5,k6)
    // }
    ROUNDDD(1, x0, x1, t0, t1, ul, tmp, KEY_0,KEY_1,KEY_2,KEY_3,KEY_4,KEY_5)
    ROUNDDD(2, x0, x1, t0, t1, ul, tmp, KEY_6,KEY_7,KEY_8,KEY_9,KEY_10,KEY_11)
    ROUNDDD(3, x0, x1, t0, t1, ul, tmp, KEY_12,KEY_13,KEY_14,KEY_15,KEY_16,KEY_17)
    ROUNDDD(4, x0, x1, t0, t1, ul, tmp, KEY_18,KEY_19,KEY_20,KEY_21,KEY_22,KEY_23)
    ROUNDDD(5, x0, x1, t0, t1, ul, tmp, KEY_24,KEY_25,KEY_26,KEY_27,KEY_28,KEY_29)
    ROUNDDD(6, x0, x1, t0, t1, ul, tmp, KEY_30,KEY_31,KEY_32,KEY_33,KEY_34,KEY_35)
    ROUNDDD(7, x0, x1, t0, t1, ul, tmp, KEY_36,KEY_37,KEY_38,KEY_39,KEY_40,KEY_41)
    ROUNDDD(8, x0, x1, t0, t1, ul, tmp, KEY_42,KEY_43,KEY_44,KEY_45,KEY_46,KEY_47)
    ROUNDDD(9, x0, x1, t0, t1, ul, tmp, KEY_48,KEY_49,KEY_50,KEY_51,KEY_52,KEY_53)
    ROUNDDD(10, x0, x1, t0, t1, ul, tmp, KEY_54,KEY_55,KEY_56,KEY_57,KEY_58,KEY_59)

    d[0] = x0;
    d[1] = x1;
}

// void decrypt(uint32_t *d) {
//     uint64_t obfvar1, obfvar2;
//     register uint64_t x0, x1, t0, t1, ul, tmp;
//     x0 = d[0];
//     x1 = d[1];
//     uint32_t *p = keys_inv+ROUND*6-1;
// //    uint32_t k1, k2;


//     for (int _=0; _<ROUND; _++) {
//     uint64_t k6=*p--, k5=*p--,k4=*p--,k3=*p--,k2=*p--,k1=*p--;
//         IN(_, tmp, x0, x1, t0, t1, ul, k3,k4,k5,k6)
//         x0 ^= tmp;
//         x1 ^= tmp;

//         x0 = x0 & MASK;
//         x1 = x1 & MASK;

//         x0 = (x0 - k1) & MASK;
//         idea_mul(_, x1, x1, k2, ul);
//     }

//     d[0] = x0;
//     d[1] = x1;
// }

// int main() {

//     uint32_t a[] = {
//             0x12345678,
//             0xdeadbeef
//     };

//         encrypt(a);
//         printf("%llx\t%llx\n", a[0], a[1]);
//         // decrypt(a);
//         // printf("%llx\t%llx\n", a[0], a[1]);
//     test();
// }

unsigned char target[] = {
    0x3e, 0xac, 0x4d, 0xc9, 0x1d, 0xf8, 0xd4, 0xb2, 0xc2, 0x08, 0xc8, 0xd9, 0xf1, 0x21, 0x3a, 0x48, 0x87, 0x56, 0x9d, 0x4e, 0x16, 0x49, 0xc6, 0xa3, 0xa4, 0x9b, 0x45, 0xa7, 0x6e, 0x30, 0xf8, 0x6f
};

// flag{0o0..MBA_0bF_1s_S0_1ntEresT1ng!!}
#define FLAG_LEN 38
int main() {
    unsigned char inputstr[50];
    puts("Your flag? ");
    scanf("%40s", inputstr);
    if (strlen(inputstr) != FLAG_LEN) {
        printf("Wrong!\n");
        exit(0);
    }
    if (inputstr[0] != 'f' ||
        inputstr[1] != 'l' ||
        inputstr[2] != 'a' ||
        inputstr[3] != 'g' ||
        inputstr[4] != '{' ||
        inputstr[FLAG_LEN-1] != '}') {
        printf("Wrong!\n");
        exit(0);
    }

    for (int i=0; i<4; i++) {
        encrypt(inputstr+5+i*8);
    }

    // for (int i=0; i<32; i++) {
    //     printf("0x%02x, ", inputstr[i+5]);
    // }
    for (int i=0; i<32; i++) {
        if (inputstr[i+5] != target[i]) {
            printf("Wrong!\n");
            exit(0);
        }
    }

    puts("Correct!");

}