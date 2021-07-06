// gcc -static-pie ./loader.c ./loader_main.c -o main
// Ubuntu 20.04

#include <stdio.h>
#include <immintrin.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

int dyn_call();

// unsigned char tmp_buf[16+1] = {32, 44, 185, 98, 172, 89, 7, 91, 150, 75, 7, 21, 45, 35, 75, 112};
unsigned char tmp_buf[16+1] = {0x9e, 0x6c, 0x47, 0x89, 0x3f, 0xb, 0x94, 0x91, 0x10, 0xf9, 0xc3, 0xa1, 0x9e, 0x7e, 0x43, 0x6f};  // hash of main_xxx
unsigned char puts_buf[16+1] = {0x79, 0xe9, 0x8, 0xc9, 0xa1, 0x2f, 0x99, 0x67, 0xa2, 0x9d, 0x5b, 0xe3, 0xe1, 0x5b, 0xdb, 0x29};  // hash of puts_xxx


// void test_main() {
//     int res = -1;
//     register __m128i exid_in asm("xmm15");
//     exid_in = _mm_loadu_si128((void*)tmp_buf);
//     __asm__ __volatile__ (
//         "mov $1, %rdi\n\t"
//         "mov $2, %rsi\n\t"
//     );
//     res = dyn_call();
//     printf("res: %d\n", res);
// }

void main_init()
{
	setvbuf(stdout,0LL, 2,0LL);
	setvbuf(stdin,0LL, 1,0LL);
	setvbuf(stderr, 0LL, 2, 0LL);
	alarm(0x3c);
}

uint32_t _my_read(uint8_t *s, uint32_t maxlen) {
    int i=0;
    while (i < maxlen) {
        read(0, s, 1);
        if (*s == '\x00' || *s == '\n') {
            return i;
        }
        i ++;
        s ++;
    }
}

void main() {
    main_init();
    puts("What's your name:");
    char name[20];
    memset(name, 0, sizeof(name));
    _my_read(name, 20);

    int res = -1;
    register __m128i exid_in asm("xmm15");
    exid_in = _mm_loadu_si128((void*)tmp_buf);
    res = dyn_call();
    // printf("main res: %d\n", res);
    
    register __m128i exid_in_ asm("xmm15");
    exid_in_ = _mm_loadu_si128((void*)puts_buf);
    ((uint64_t (*)(void *, void *, void *))(*(void **)(0x300000)))(name, 0, 0);
}