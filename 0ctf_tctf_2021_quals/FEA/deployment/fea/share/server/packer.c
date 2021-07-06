// gcc packer.c fastlz.c -g -o packer
// ./packer ./iEKrWcvgR9ZlsfeH ./iEKrWcvgR9ZlsfeH_out

#include "fastlz.h"
#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>

// #define DEBUG
// #include "code.h"

int file_size(char* filename)
{
    struct stat statbuf;
    stat(filename,&statbuf);
    int size=statbuf.st_size;
 
    return size;
}

uint8_t* readfile(char *filename, int size) {
    int fd = open(filename, O_RDONLY);
    if(-1 == fd){
		printf("file open error!\n");
		exit(0);
	}

    uint8_t * buf = malloc(size);

    int len = read(fd, buf, size);
    if(len < 0) {
        printf("file read error!\n");
		exit(0);
    }

    close(fd);
    return buf;
}

int findUserCodeBegin(u_int8_t * buf, int size) {
    int lastfuncbegin = 0;
    for (int i=0; i < size-4; i++) {
        if (buf[i] == 0x55 &&
            buf[i+1] == 0x48 &&
            buf[i+2] == 0x89 &&
            buf[i+3] == 0xe5) {
                if (i-lastfuncbegin > 0x10000) {
                    // return lastfuncbegin-0x10;          // try to avoid F3 0F 1E FA                             endbr64
                    return lastfuncbegin;
                }
                lastfuncbegin = i;
            }
    }
    return -1;
}

int findUserCodeMain(u_int8_t * buf, int size, int begin) {
    int cnt = 0;
    for (int i=begin; i < size-4; i++) {
        if (buf[i] == 0x55 &&
            buf[i+1] == 0x48 &&
            buf[i+2] == 0x89 &&
            buf[i+3] == 0xe5) {
                cnt += 1;
                if (cnt >= 4) {
                    return i;
                }
            }
    }
}

int findUserCodeEnd(u_int8_t * buf, int size, int begin) {
    int cnt = 0;
    for (int i=begin; i < size-7; i++) {
        if (buf[i] == 0x41 &&
            buf[i+1] == 0x57 &&
            buf[i+2] == 0x41 &&
            buf[i+3] == 0x56 &&
            buf[i+4] == 0x49) {
                // cnt += 1;
                // if (cnt >= 6) {
                //     return i-1;
                // }
                return i;
            }
        if (buf[i] == 0x41 &&
            buf[i+1] == 0x56 &&
            buf[i+5] == 0x41 &&
            buf[i+6] == 0x55) {
                return i;
            }
    }
}

void savetofile(u_int8_t * buf, int size, int ep) {
    int fd = open("./code.h", O_WRONLY | O_CREAT | O_TRUNC);
    if(-1 == fd){
		printf("file open error!\n");
		exit(0);
	}
    char a[] = "int ep = ";
    write(fd, a, sizeof(a)-1);
    uint8_t *t = malloc(50);
    sprintf(t, "0x%x;\n", ep);
    write(fd, t, strlen(t));

    char b[] = "unsigned char code[] = { ";
    write(fd, b, sizeof(b)-1);

    uint8_t * tmp = malloc(size*6);
    memset(tmp, 0, size*6);
    
    for (int i=0; i<size; i++) {
        sprintf(tmp+(5*i), "0x%02x,", buf[i]);
    }

    int w = write(fd, tmp, size*5);
    
    #ifdef DEBUG
    printf("size: 0x%x\n", size);
    printf("w: 0x%x\n", w);
    printf("size*5: 0x%x\n", size*5);
    #endif

    char e[] = "};";
    write(fd, e, sizeof(e)-1);

    close(fd);
}

int main(int argc, char *argv[]) {
    if( argc <= 2 )
    {
        printf("[*] Usage: %s filename output_filename\n", argv[0]);
        exit(0);
    }

    char * filename = argv[1];
    char * output_filename = argv[2];

    int filesize = file_size(filename);
    char *filebuf = readfile(filename, filesize);

    int begin = findUserCodeBegin(filebuf, filesize);
    int end = findUserCodeEnd(filebuf, filesize, begin);
    // int end = filesize;
    int main_addr = findUserCodeMain(filebuf, filesize, begin);

    uint8_t * compressed_buf = (uint8_t *)malloc(end-begin+10);
    memset(compressed_buf, 0, end-begin+10);

    int compressed_size = fastlz_compress((void *)(filebuf+begin), end-begin, (void *)compressed_buf);

    savetofile(compressed_buf, compressed_size, main_addr-begin);


    #ifdef DEBUG
    printf("begin: 0x%x\nend: 0x%x\nmain_addr: 0x%x\nlen:0x%x\ncompressed_size: 0x%x\n", begin, end, main_addr, end-begin, compressed_size);

    uint8_t * decompressed_buf = (uint8_t *)malloc(end-begin+10);
    memset(decompressed_buf, 0, end-begin+10);
    int decompressed_size = fastlz_decompress((void *)compressed_buf, compressed_size, decompressed_buf, 0xFFFFFF);
    printf("[DEBUG] decompress_size: 0x%x\n", decompressed_size);
    for (int i=0; i<end-begin; i++) {
        if (decompressed_buf[i] != ((uint8_t *)filebuf)[begin+i]) {
            printf("%d\t%x %x\n", i, ((uint8_t *)filebuf)[begin+i], decompressed_buf[i]);
        }
    }
    // for (int i=0; i<compressed_size; i++) {
    //     if (compressed_buf[i] != ((uint8_t *)code)[i]) {
    //         printf("%d\t%x %x\n", i, ((uint8_t *)code)[i], compressed_buf[i]);
    //     }
    // }
    // printf("ep: 0x%x\n", decompressed_buf[ep]);
    #endif

    #ifdef DEBUG
    // char cmd[100] = "gcc final.c fastlz.c -Wimplicit-function-declaration -o ";
    char cmd[200] = "/home/pwn/clang -mllvm -bcf -mllvm -fla -mllvm -sobf -I/home/pwn/include/ final.c fastlz.c -Wimplicit-function-declaration -o ";
    #endif
    #ifndef DEBUG
    // char cmd[100] = "gcc final.c fastlz.c -s -Wimplicit-function-declaration -o ";
    char cmd[200] = "/home/pwn/clang -mllvm -bcf -mllvm -fla -mllvm -sobf -I/home/pwn/include/ final.c fastlz.c -s -Wimplicit-function-declaration -o ";
    #endif
    strcat(cmd, output_filename);
    system(cmd);
    return 0;
}