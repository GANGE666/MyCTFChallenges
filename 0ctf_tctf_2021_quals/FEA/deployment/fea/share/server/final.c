#include "code.h"

// gcc source.c -o pwn -lseccomp -fPIE -pie -z now

#include <fcntl.h>             // 提供open()函数  
#include <unistd.h>  
#include <stdint.h>
#include <stdio.h>  
#include <dirent.h>            // 提供目录流操作函数  
#include <string.h>  
#include <sys/stat.h>        // 提供属性操作函数  
#include <sys/types.h>         // 提供mode_t 类型  
#include <stdlib.h> 
// #include <seccomp.h>
// #include <linux/seccomp.h>
#include <sys/mman.h>
#include <signal.h>
#include <sys/ptrace.h>

#define RES_ADDR 0xdead0000

// #define DEBUG
void illegal2() {
    __asm__ __volatile__ (".byte 0xE8\n\t");
}

int cnt_0xCC();

void SIGTRAP_handler(int signo)
{
    *(uint32_t *)(RES_ADDR) ^= 0xdeadbeef;
}

int gv_alarm = 0;
char name[1024];
char name2[1024];
pid_t ppid;
int cc = 0;

void SIGALRM_handler(int signo) {
    if (gv_alarm == 0) {
        gv_alarm = 1;
        alarm(300);
    } else {
        printf("Timeout\n");
        exit(0);
    }
}

int get_name_by_pid(pid_t pid, char* name)
{
    int fd;
    char buf[1024] = {0};
    snprintf(buf, 1024, "/proc/%d/cmdline", pid);
    if ((fd = open(buf, O_RDONLY)) == -1)
        return -1;
    read(fd, buf, 1024);
    strncpy(name, buf, 1023);
    close(fd);
    return 0;
}

void init() {
    setvbuf(stdout,0LL,2,0LL);
	setvbuf(stdin,0LL,1,0LL);
	setvbuf(stderr, 0LL, 2, 0LL);
    signal(SIGTRAP, SIGTRAP_handler);

    ppid = getppid();
    if (get_name_by_pid(ppid, name)) exit(0);
 
} 

void illegal() {
    __asm__ __volatile__ (".byte 0x00\n\t");
}

void check() {
    if (get_name_by_pid(ppid, name2)) exit(0);
    // printf("name: %s\n", name);
    // printf("name2: %s\n", name2);
    if (
        strcmp(name, "gdb") == 0 ||
        strcmp(name, "strace") == 0 ||
        strcmp(name, "ltrace") == 0 ||
        strcmp(name, "linux_server64") == 0) {
            illegal();
        }
    if (strcmp(name2, name) != 0) {
        illegal();
    }
}

int main(int argc, char *argv[])  
{
	init();  

    void *mem = mmap(0, 0x100000, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_ANON|MAP_PRIVATE, -1, 0);
    memset(mem, 0, 0x100000);
    if(mem == MAP_FAILED)
    {
        perror("mmap");
        exit(-1);
    }
    check();

    while(gv_alarm == 0) {
        if (cnt_0xCC() != cc) {
            illegal2();
        }
        usleep(100000);
    }

    // memcpy(mem, code, sizeof(code));
    int ret = fastlz_decompress((void *)code, (int)sizeof(code), mem, 0xFFFFFF);
    if (ret == 0) {
        perror("load fail");
        exit(-1);
    }
    check();

    #ifdef DEBUG
    printf("fastlz_decompress:\n\tret: 0x%x\n\tsizeof(code): 0x%x\n", ret, (int)sizeof(code));
    #endif

    int (*func)();
    func = (int (*)())(mem+ep);
    (int)(*func)();

err:
    munmap(mem, 0x100000);

    return 0;  
}


__attribute__((constructor))
void init_anti() {
    // if ( ptrace(PTRACE_TRACEME, 0, 1, 0) < 0 ) {
    //     printf("traced!\n");
    //     // exit(0);
    // }
    signal(SIGALRM, SIGALRM_handler);
    alarm(1);
    cc = cnt_0xCC();

    void *mem = mmap(RES_ADDR, 0x1000, PROT_READ|PROT_WRITE, MAP_ANON|MAP_PRIVATE, -1, 0);
    memset(mem, 0, 0x1000);
    if(mem == MAP_FAILED)
    {
        perror("mmap");
        exit(-1);
    }
}

int cnt_0xCC() {
    int cnt = 0;
    for(uint64_t i=illegal2; i<cnt_0xCC; i++) {
        if( *(uint8_t *)i == 0xCC) {
            cnt += 1;
        }
    }
    return cnt;
}