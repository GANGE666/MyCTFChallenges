// gcc loader.c loader_main.c -o main

#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <immintrin.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <error.h>
#include <stdint.h>
#include "assert.h" 


#include "loader_struct.h"

#define LOADER_DEBUG

// gcc -static-pie -Wl,-gc-sections  ./loader.c -o loader
// gcc -shared -fPIC -static-pie -Wl,-gc-sections ./loader.c -o loader.so

u_int8_t ToHexLower(u_int8_t value) 
{
	return "0123456789abcdef"[value & 0xF];
}

void digest2hexdigest(u_int8_t* in, u_int8_t* out) {
    for (int i=0; i < 16; i++) {
        out[2*i] = ToHexLower(in[i] >> 4);
        out[2*i+1] = ToHexLower(in[i] & 0xf);
    }
}



void* load(func_block_st* block) {
    register __m128i exid asm("xmm15");
    u_int8_t exid_buf[16+1];
    memset(exid_buf, 0, sizeof(exid_buf));
    _mm_storeu_si128((void*)exid_buf, exid);

    // u_int8_t hex_exid_buf[32+1];
    // memset(hex_exid_buf, 0, sizeof(hex_exid_buf));
    // digest2hexdigest(exid_buf, hex_exid_buf);
    digest2hexdigest(exid_buf, block->id);
    // printf("%s\n", block->id);

    int fd, nread;
    struct stat sb;
    void *mapped;

    if((fd = open(block->id, O_RDONLY)) < 0){
        perror("open");
        puts(block->id);
        exit(-1);
    }   

    if((fstat(fd, &sb)) == -1 ){
        perror("fstat") ;
        exit(-1);
    }
    uint32_t addr = rand() & 0xfffff000;
    while (addr <= 0x10000000) {
        addr = rand() & 0xfffff000;
    }

    // if((mapped = mmap(NULL, sb.st_size, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_ANON|MAP_PRIVATE, fd, 0)) ==(void*) -1){
    if((mapped = mmap(addr, sb.st_size, PROT_READ|PROT_EXEC, MAP_SHARED|MAP_FIXED_NOREPLACE, fd, 0)) ==(void*) -1){
        perror("mmap") ;
        exit(-1);
    }

    block->mmap_addr = mapped;
    block->mmap_size = sb.st_size;
    #ifdef LOADER_DEBUG
    // fprintf(stderr, "mapped %s at: %p\n", block->id, mapped);
    #endif 

    close(fd);

    return mapped;
}

int func_block_cnt = 0;
func_block_st* root;

void* do_load() {
    func_block_st* block = (func_block_st*) malloc(sizeof(func_block_st));
    memset(block, 0, sizeof(func_block_st));
    block->retaddr = __builtin_return_address(1);
    #ifdef LOADER_DEBUG
    // fprintf(stderr, "calling from %p - x\n", block->retaddr);
    #endif

    // if (root != 0){
    //     block->next = root->next;
    //     root->next = block;
    // }
    block->next = root;
    root = block;
    func_block_cnt ++;
    
    return load(block);
}

void* do_unload() {
    assert(root != 0);
    void* origin_ret_address = root->retaddr;
    munmap(root->mmap_addr, root->mmap_size);
    func_block_st* next = root->next;
    free(root);
    root = next;
    func_block_cnt --;

    #ifdef LOADER_DEBUG
    // fprintf(stderr, "returning to %p\n", origin_ret_address);
    #endif
    return origin_ret_address;
}

// void dyn_call(){
//     register void* mapped asm("rbx");
//     __asm__ __volatile__ (
//         "push %rdi\n\t"
//         "push %rsi\n\t"
//         "push %rdx\n\t"
//         "push %rcx\n\t"
//         "push %r8\n\t"
//         "push %r9\n\t"
//         );
//     mapped = load();
    
//     // void (*func)();
//     // func = mapped;
//     __asm__ __volatile__ (
//         "pop %r9\n\t"
//         "pop %r8\n\t"
//         "pop %rcx\n\t"
//         "pop %rdx\n\t"
//         "pop %rsi\n\t"
//         "pop %rdi\n\t"
//         );
//     ((void (*)())mapped)();
// }

void* dyn_call() {
    __asm__ __volatile__ (
        "push %rdi\n\t"
        "push %rsi\n\t"
        "push %rdx\n\t"
        "push %rcx\n\t"
        "push %r8\n\t"
        "push %r9\n\t"
        "call do_load\n\t"              // mark origin return addr
        "pop %r9\n\t"
        "pop %r8\n\t"
        "pop %rcx\n\t"
        "pop %rdx\n\t"
        "pop %rsi\n\t"
        "pop %rdi\n\t"

        "pop %rbp\n\t"
        "add $8, %rsp\n\t"              // remove origin return addr
        
        "call %rax\n\t"                 // jmp or call
        "push %rax\n\t"                 // save call result
        
        "call do_unload\n\t"
        "pop %rdi\n\t"
        "push %rax\n\t"                 // set origin return addr
        "mov %rdi, %rax\n\t"
        "ret"
    );
}

// void* mapped;
// void dyn_call_2(void *a0, void *a1, void *a2, void *a3, void *a4, void *a5) {
//     mapped = load();
//     ((void (*)(void *, void *, void *, void *, void *, void *))mapped)(a0, a1, a2, a3, a4, a5);     // patch to jmp?
    
// }

#define PROXY_ADDR 0x300000

__attribute__((constructor))
void init() {
    // copy dyn_call address to a solid address
    void *mem = mmap((void *)PROXY_ADDR, 0x1000, PROT_READ|PROT_WRITE, MAP_ANON|MAP_PRIVATE, -1, 0);
    if(mem == MAP_FAILED)
    {
        perror("mmap");
        exit(-1);
    }

    *((void **)mem) = (void *)dyn_call;

    mprotect(mem, 0x1000, PROT_READ);
    // printf("load .PROXY_ADDR at %p\n", mem);
}

#define BSS_BASE 0x700000000
#define RODATA_BASE 0x600000000

__attribute__((constructor))
void init_rodata() {
    int fd;
    struct stat sb;
    void *mapped;

    if((fd = open("rodata", O_RDONLY)) < 0){
        perror("open") ;
        exit(-1);
    }   

    if((fstat(fd, &sb)) == -1 ){
        perror("fstat") ;
        exit(-1);
    }   
    if((mapped = mmap(RODATA_BASE, sb.st_size, PROT_READ, MAP_SHARED, fd, 0)) ==(void*) -1){
        perror("mmap") ;
        exit(-1);
    }

    close(fd);
    // printf("load .rodata at %p\n", mapped);
}

__attribute__((constructor))
void init_bss() {
    void *mem = mmap((void *)BSS_BASE, 0x10000, PROT_READ|PROT_WRITE, MAP_ANON|MAP_PRIVATE, -1, 0);
    if(mem == MAP_FAILED)
    {
        perror("mmap");
        exit(-1);
    }
    // printf("load .bss at %p\n", mem);
}

// u_int8_t tmp_buf[16+1] = " ,\xb9b\xacY\x07[\x96K\x07\x15-#Kp";

// int main() {
//     register __m128i exid_in asm("xmm15");
    
//     exid_in = _mm_loadu_si128((void*)tmp_buf);
//     dyn_call_2(0,0,0,0,0,0);
// }