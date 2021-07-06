//
// Created by G6 on 2020-06-21.
//
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define XORSHIFT(x) (((x ^( x << 13)) ^ ((x ^( x << 13)) >> 17)) ^ (((x ^( x << 13)) ^ ((x ^( x << 13)) >> 17)) << 5))

#define TIME_COMSUMER(x) \
({\
    uint32_t i; \
    uint32_t res; \
    res = x; \
    for (i = 0; i < 100000; i=i+1) {\
        res = XORSHIFT(res); \
    } \
    res; \
})

//uint32_t xorshift(uint32_t state)
//{
//    /* Algorithm "xor" from p. 4 of Marsaglia, "Xorshift RNGs" */
//    uint32_t x = state;
//    x ^= x << 13;
//    x ^= x >> 17;
//    x ^= x << 5;
//    return x;
//}
//


//int test() {
////    for (uint32_t i = 0; i <= 0xFFFFFFF0; i++) {
////        if (i %0xFFFFFFF == 0) {
////            puts("1");
////        }
////        if (TIME_COMSUMER(i) == 0x369d0854) {
////            printf("%x 0x%x\n", i, TIME_COMSUMER(i));
////        }
////    }
//
//    uint32_t a[] = {1734437990, 1497712763 ^ 0xAAAAAAAA, 1836403745, 555841904 ^ 0xAAAAAAAA, 1668563031, 1966104392 ^ 0xAAAAAAAA, 2035113844, 1165120607 ^ 0xAAAAAAAA, 2099323237};
//
//    for (int i=0; i<9; i++) {
//        printf("%x 0x%x\n", a[i], TIME_COMSUMER(a[i]));
//    }
//}


#define ELSE_ERROR else {puts("Ow!"); return;}

#define NUM1 (((((((1*2*2*2*5 + 1)*2*2*5 + 1)*2*2*5 + 1)*2*2*2*2*2 + 1)*2 + 1)*2*2*3*3*3*3 + 1)*2*2 + 1)*2
#define NUM2 (((((1*2*3*3 + 1)*2*5 + 1)*2*3*5 + 1)*2*3*3 + 1)*2*3*3*3 + 1)*2
#define NUM3 ((((((1*2*5 + 1)*2 + 1)*2*2*3 + 1)*2*2 + 1)*2*2*2*5*5*5*5 + 1)*2*2*3*5*5 + 1)*2
#define NUM4 ((((((((1*2*5 + 1)*2 + 1)*2*2*2*3*3 + 1)*2*2*2*2*2*5 + 1)*2 + 1)*2 + 1)*2*3 + 1)*2*2 + 1)*2*2*3*3
#define NUM5 ((((((((((1*2*2*3 + 1)*2*2*3*5 + 1)*2*5 + 1)*2*3 + 1)*2*3 + 1)*2*3 + 1)*2*5 + 1)*2 + 1)*2*2*5 + 1)*2*3 + 1)
#define NUM6 (((((((((1*2*3 + 1)*2*2*2*2 + 1)*2 + 1)*2*2*2*2*2*3 + 1)*2*2 + 1)*2*2*2*3 + 1)*2*2 + 1)*2*3 + 1)*2*2 + 1)*3*3
#define NUM7 (((((((1*2*3*3 + 1)*2*2*2*5 + 1)*2*2*2 + 1)*2 + 1)*2*2*3*3*3*3 + 1)*2*3 + 1)*2*3 + 1)*3
#define NUM8 ((((((((((1*2*3 + 1)*2*3 + 1)*2*2*2*5 + 1)*2 + 1)*2*3*5 + 1)*2*3 + 1)*2*2 + 1)*2 + 1)*2*2*3*5 + 1)*2*2*3 + 1)
#define NUM9 ((((1*2*5 + 1)*2*2*2*3*3*3 + 1)*2*2 + 1)*2*2*2*2*2*2*2*2*3*3*5 + 1)*3*3*3

//#define NUM1 0xa25dc66a
//#define NUM2 0xaa0036
//#define NUM3 0xc64e001a
//#define NUM4 0x369d0854
//#define NUM5 0xf15bcf8f
//#define NUM6 0x6bbe1965
//#define NUM7 0x1966cd91
//#define NUM8 0xd4c5fbfd
//#define NUM9 0xb04a9b1b

// 0xAAAAAAAA
#define XOE_NUM (((((((((1*2*3 + 1)*2*3 + 1)*2*5 + 1)*2 + 1)*2*3*3*3 + 1)*2*2 + 1)*2 + 1)*2*2*2*2*3 + 1)*2*2*2*2 + 1)*2*5

// flag{HEY!Lumpy!!W@tcH_0ut_My_TrEe!!}

void main() {
//    test();
    uint32_t input_str[20];
    memset(input_str, 0, 80);
    puts("Ah?");
    scanf("%36s", input_str);

    if (    (TIME_COMSUMER(input_str[0]) == NUM1) &&
            (TIME_COMSUMER((input_str[1] ^ XOE_NUM)) == NUM2) &&
            (TIME_COMSUMER(input_str[2]) == NUM3) &&
            (TIME_COMSUMER((input_str[3] ^ XOE_NUM)) == NUM4) &&
            (TIME_COMSUMER(input_str[4]) == NUM5) &&
            (TIME_COMSUMER((input_str[5] ^ XOE_NUM)) == NUM6) &&
            (TIME_COMSUMER(input_str[6]) == NUM7) &&
            (TIME_COMSUMER((input_str[7] ^ XOE_NUM)) == NUM8) &&
            (TIME_COMSUMER(input_str[8]) == NUM9)) {
        puts("Wow!");
        return;
    } ELSE_ERROR
}
