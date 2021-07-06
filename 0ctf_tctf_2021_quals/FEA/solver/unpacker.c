//
// Created by G6 on 2021-06-24.
//

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


int file_size(char* filename)
{
    struct stat statbuf;
    stat(filename,&statbuf);
    unsigned int size=statbuf.st_size;

    return size;
}

uint8_t* readfile(char *filename, int size) {
    int fd = open(filename, O_RDONLY);
    if(-1 == fd){
        printf("file open error!\n");
        exit(0);
    }

    uint8_t * buf = malloc(size);

    ssize_t len = read(fd, buf, size);
    if(len < 0) {
        printf("file read error!\n");
        exit(0);
    }

    close(fd);
    return buf;
}

void writefile(char *filename, uint8_t *buf, unsigned int size) {
    int fd = open(filename, O_WRONLY|O_CREAT, S_IRWXU|S_IRWXG|S_IRWXO);
    if(-1 == fd){
        printf("file open error!\n");
        exit(0);
    }

    write(fd, buf, size);

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

    uint8_t * decompressed_buf = (uint8_t *)malloc(0x200000);
    memset(decompressed_buf, 0, 0x200000);
    int decompressed_size = fastlz_decompress((void *)filebuf, filesize, decompressed_buf, 0xFFFFFF);

    writefile(output_filename, decompressed_buf, decompressed_size);

    return 0;
}
