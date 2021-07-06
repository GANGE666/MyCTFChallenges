#include "rodata_proxy.h"
#include "bss_proxy.h"
#include "function_proxy.h"

#define __INT3__ __asm__ __volatile__ (    \
        ".byte 0xcc\n\t"    \
);

#define __RELEASE__

/************************************************************************

heap.h

*/

#ifndef HEAP_H
#define HEAP_H

#include <stdint.h>
#include <stddef.h>

#define HEAP_INIT_SIZE 0x10000
#define HEAP_MAX_SIZE 0xF0000
#define HEAP_MIN_SIZE 0x10000

#define MIN_ALLOC_SZ 4

#define MIN_WILDERNESS 0x2000
#define MAX_WILDERNESS 0x1000000

#define BIN_COUNT 9
#define BIN_MAX_IDX (BIN_COUNT - 1)

typedef unsigned int uint;

typedef struct node_t {
    uint hole;
    uint size;
    struct node_t* next;
    struct node_t* prev;
} node_t;

typedef struct { 
    node_t *header;
} footer_t;

typedef struct {
    node_t* head;
} bin_t;

typedef struct {
    long start;
    long end;
    bin_t *bins[BIN_COUNT];
} heap_t;

// extern const uint overhead;

void init_heap(heap_t *heap, long start);

void *heap_alloc(heap_t *heap, size_t size);
void heap_free(heap_t *heap, void *p);
uint expand(heap_t *heap, size_t sz);
void contract(heap_t *heap, size_t sz);

uint get_bin_index(size_t sz);
void create_foot(node_t *head);
footer_t *get_foot(node_t *head);

node_t *get_wilderness(heap_t *heap);

#endif


/************************************************************************

llist.h

*/

#ifndef LLIST_H
#define LLIST_H

#include <stdint.h>

void add_node(bin_t *bin, node_t *node);

void remove_node(bin_t *bin, node_t *node);

node_t *get_best_fit(bin_t *list, size_t size);
node_t *get_last_node(bin_t *list);

node_t *next(node_t *current);
node_t *prev(node_t *current);

#endif



/************************************************************************

llist.c

*/
void add_node(bin_t *bin, node_t* node) {
    node->next = NULL;
    node->prev = NULL;

    node_t *temp = bin->head;

    if (bin->head == NULL) {
        bin->head = node;
        return;
    }
    
    // we need to save next and prev while we iterate
    node_t *current = bin->head;
    node_t *previous = NULL;
    // iterate until we get the the end of the list or we find a 
    // node whose size is
    while (current != NULL && current->size <= node->size) {
        previous = current;
        current = current->next;
    }

    if (current == NULL) { // we reached the end of the list
        previous->next = node;
        node->prev = previous;
    }
    else {
        if (previous != NULL) { // middle of list, connect all links!
            node->next = current;
            previous->next = node;

            node->prev = previous;
            current->prev = node;
        }
        else { // head is the only element
            node->next = bin->head;
            bin->head->prev = node;
            bin->head = node;
        }
    }
}

void remove_node(bin_t * bin, node_t *node) {
    if (bin->head == NULL) return; 
    if (bin->head == node) { 
        bin->head = bin->head->next;
        return;
    }
    
    node_t *temp = bin->head->next;
    while (temp != NULL) {
        if (temp == node) { // found the node
            if (temp->next == NULL) { // last item
                temp->prev->next = NULL;
            }
            else { // middle item
                temp->prev->next = temp->next;
                temp->next->prev = temp->prev;
            }
            // we dont worry about deleting the head here because we already checked that
            return;
        }
        temp = temp->next;
    }
}

node_t *get_best_fit(bin_t *bin, size_t size) {
    if (bin->head == NULL) return NULL; // empty list!

    node_t *temp = bin->head;

    while (temp != NULL) {
        if (temp->size >= size) {
            return temp; // found a fit!
        }
        temp = temp->next;
    }
    return NULL; // no fit!
}

node_t *get_last_node(bin_t *bin) {
    node_t *temp = bin->head;

    while (temp->next != NULL) {
        temp = temp->next;
    }
    return temp;
}




/************************************************************************

malloc.c

*/
const uint offset = 8;
const uint overhead = sizeof(footer_t) + sizeof(node_t);

void init_heap(heap_t *heap, long start) {
    node_t *init_region = (node_t *) start;
    init_region->hole = 1;
    init_region->size = (HEAP_INIT_SIZE) - sizeof(node_t) - sizeof(footer_t);

    FUNCTION_create_foot(init_region);

    register int tmp = FUNCTION_get_bin_index(init_region->size);
    FUNCTION_add_node(heap->bins[tmp], init_region);

    heap->start = (void *) start;
    heap->end   = (void *) (start + HEAP_INIT_SIZE);
}

void *heap_alloc(heap_t *heap, size_t size) {
    uint index = FUNCTION_get_bin_index(size);
    bin_t *temp = (bin_t *) heap->bins[index];
    node_t *found = FUNCTION_get_best_fit(temp, size);

    while (found == NULL) {
        if (index + 1 >= BIN_COUNT) {
            return NULL;
        }

        temp = heap->bins[++index];
        found = FUNCTION_get_best_fit(temp, size);
    }
    
    if ((found->size - size) > (S_overhead + MIN_ALLOC_SZ)) {
        
        node_t *split = (node_t *) (((char *) found + sizeof(node_t) + sizeof(footer_t)) + size);
        split->size = found->size - size - sizeof(node_t) - sizeof(footer_t);
        split->hole = 1;
   
        FUNCTION_create_foot(split);
        
        uint new_idx = FUNCTION_get_bin_index(split->size);
        
        FUNCTION_add_node(heap->bins[new_idx], split); 

        found->size = size; 
        FUNCTION_create_foot(found); 
    }

    found->hole = 0; 
    FUNCTION_remove_node(heap->bins[index], found); 
    
    node_t *wild = FUNCTION_get_wilderness(heap);
    if (wild->size < MIN_WILDERNESS) {
        uint success = FUNCTION_expand(heap, 0x1000);
        if (success == 0) {
            return NULL;
        }
    }
    else if (wild->size > MAX_WILDERNESS) {
        FUNCTION_contract(heap, 0x1000);
    }

    found->prev = NULL;
    found->next = NULL;
    return &found->next; 
}

void heap_free(heap_t *heap, void *p) {
    bin_t *list;
    footer_t *new_foot, *old_foot;

    node_t *head = (node_t *) ((char *) p - S_offset);
    if (head == (node_t *) (uintptr_t) heap->start) {
        head->hole = 1; 

        register int tmp = FUNCTION_get_bin_index(head->size);
        FUNCTION_add_node(heap->bins[tmp], head);
        return;
    }

    node_t *next = (node_t *) ((char *) FUNCTION_get_foot(head) + sizeof(footer_t));
    footer_t *f = (footer_t *) ((char *) head - sizeof(footer_t));
    node_t *prev = f->header;
    
    if (prev->hole) {
        list = heap->bins[FUNCTION_get_bin_index(prev->size)];
        FUNCTION_remove_node(list, prev);

        prev->size += S_overhead + head->size;
        new_foot = FUNCTION_get_foot(head);
        new_foot->header = prev;

        head = prev;
    }

    if (next->hole) {
        list = heap->bins[FUNCTION_get_bin_index(next->size)];
        FUNCTION_remove_node(list, next);

        head->size += S_overhead + next->size;

        old_foot = FUNCTION_get_foot(next);
        old_foot->header = 0;
        next->size = 0;
        next->hole = 0;
        
        new_foot = FUNCTION_get_foot(head);
        new_foot->header = head;
    }

    head->hole = 1;
    register int tmp = FUNCTION_get_bin_index(head->size);
    FUNCTION_add_node(heap->bins[tmp], head);
}

uint expand(heap_t *heap, size_t sz) {
    return 0;
}

void contract(heap_t *heap, size_t sz) {
    return;
}

uint get_bin_index(size_t sz) {
    uint index = 0;
    sz = sz < 4 ? 4 : sz;

    while (sz >>= 1) index++; 
    index -= 2; 
    
    if (index > BIN_MAX_IDX) index = BIN_MAX_IDX; 
    return index;
}

void create_foot(node_t *head) {
    footer_t *foot = FUNCTION_get_foot(head);
    foot->header = head;
}

footer_t *get_foot(node_t *node) {
    return (footer_t *) ((char *) node + sizeof(node_t) + node->size);
}

node_t *get_wilderness(heap_t *heap) {
    footer_t *wild_foot = (footer_t *) ((char *) heap->end - sizeof(footer_t));
    return wild_foot->header;
}




/************************************************************************

tinylib.c

*/



static  long __syscall0(long n)
{
	unsigned long ret;
	__asm__ __volatile__ ("syscall" : "=a"(ret) : "a"(n) : "rcx", "r11", "memory");
	return ret;
}

static  long __syscall1(long n, long a1)
{
	unsigned long ret;
	__asm__ __volatile__ ("syscall" : "=a"(ret) : "a"(n), "D"(a1) : "rcx", "r11", "memory");
	return ret;
}

static  long __syscall2(long n, long a1, long a2)
{
	unsigned long ret;
	__asm__ __volatile__ ("syscall" : "=a"(ret) : "a"(n), "D"(a1), "S"(a2)
						  : "rcx", "r11", "memory");
	return ret;
}

static  long __syscall3(long n, long a1, long a2, long a3)
{
	unsigned long ret;
	__asm__ __volatile__ ("syscall" : "=a"(ret) : "a"(n), "D"(a1), "S"(a2),
						  "d"(a3) : "rcx", "r11", "memory");
	return ret;
}

static  long __syscall4(long n, long a1, long a2, long a3, long a4)
{
	unsigned long ret;
	register long r10 __asm__("r10") = a4;
	__asm__ __volatile__ ("syscall" : "=a"(ret) : "a"(n), "D"(a1), "S"(a2),
						  "d"(a3), "r"(r10): "rcx", "r11", "memory");
	return ret;
}

static  long __syscall5(long n, long a1, long a2, long a3, long a4, long a5)
{
	unsigned long ret;
	register long r10 __asm__("r10") = a4;
	register long r8 __asm__("r8") = a5;
	__asm__ __volatile__ ("syscall" : "=a"(ret) : "a"(n), "D"(a1), "S"(a2),
						  "d"(a3), "r"(r10), "r"(r8) : "rcx", "r11", "memory");
	return ret;
}

static  long __syscall6(long n, long a1, long a2, long a3, long a4, long a5, long a6)
{
	unsigned long ret;
	register long r10 __asm__("r10") = a4;
	register long r8 __asm__("r8") = a5;
	register long r9 __asm__("r9") = a6;
	__asm__ __volatile__ ("syscall" : "=a"(ret) : "a"(n), "D"(a1), "S"(a2),
						  "d"(a3), "r"(r10), "r"(r8), "r"(r9) : "rcx", "r11", "memory");
	return ret;
}

// =============================================================================

  ssize_t tiny_read(int fd, void *buf, size_t count) {
	return (ssize_t)FUNCTION___syscall3(0, (long)fd, (long)buf, (long)count);
}

  ssize_t tiny_write(int fd, const void *buf, size_t count) {
	return (ssize_t)FUNCTION___syscall3(1, (long)fd, (long)buf, (long)count);
}

#define O_RDONLY 0
#define O_WRONLY 1
#define O_RDWR 2

  int tiny_open(const char *pathname, int flags) {
	return (int)FUNCTION___syscall2(2, (long)pathname, flags);
}

  int tiny_close(int fd) {
	return (int)FUNCTION___syscall1(3, (long)fd);
}

#define MAP_SHARED     0x01
#define MAP_PRIVATE    0x02
#define MAP_ANONYMOUS  0x20
#define MAP_NORESERVE  0x4000
#define PROT_NONE      0
#define PROT_READ      1
#define PROT_WRITE     2
#define PROT_EXEC      4

  void *tiny_mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset_) {
	return (void *)FUNCTION___syscall6(9, (long)addr, (long)length, (long)prot, (long)flags, (long)fd, (long)offset_);
}

  int tiny_munmap(void *addr, size_t length) {
	return (int)FUNCTION___syscall2(11, (long)addr, (long)length);
}

  int tiny_execve(const char *pathname, char *const argv[], char *const envp[]) {
	return (int)FUNCTION___syscall3(59, (long)pathname, (long)argv, (long)envp);
}

  void tiny_exit(int status) {
	FUNCTION___syscall1(60, (long)status);
}



/************************************************************************

mylib.h

*/
#include <unistd.h>
#include <sys/syscall.h>   /* For SYS_xxx definitions */
#include <stdint.h>

#ifndef MYLIB
#define MYLIB

uint64_t rand_seed;

__attribute__((noinline))
uint32_t my_syscall(int a, ...);


uint32_t my_strlen(uint8_t *s);

void my_strcpy(uint8_t* dst, uint8_t* src);

void my_puts(uint8_t *s);

uint32_t my_read(uint8_t *s, uint32_t maxlen);

void my_srand(uint32_t seed);

uint32_t my_rand();

void my_exit(uint32_t code);

char *my_itoa(char *p, uint32_t x);

int isdigit(int c);

int isspace(int c);

int my_atoi(const char *s);

int my_readint();


#endif 


/************************************************************************

mylib.c

*/



// uint64_t rand_seed = 0;

__attribute__((noinline))
uint32_t my_syscall(int a, ...) {
    __asm__ __volatile__ (
        "movq %rdi, %rax\n\t"       /* Syscall number -> rax.  */
        "movq %rsi, %rdi\n\t"
        "movq %rdx, %rsi\n\t"
        "movq %rcx, %rdx\n\t"
        "syscall\n\t"
        );
    return;
}


uint32_t my_strlen(uint8_t *s) {
    uint32_t cnt = 0;
    while (*s)
    {
        cnt++;
        s++;
    }
    return cnt;
}

void my_strcpy(uint8_t* dst, uint8_t* src) {
    int len = FUNCTION_my_strlen(src);
    for (int i=0; i<len; i++) {
        *dst = *src;
        dst++;
        src++;
    }
}

void my_puts(uint8_t *s) {
    // FUNCTION_my_syscall(SYS_write, 1, s, FUNCTION_my_strlen(s));
    register int len = FUNCTION_my_strlen(s);
    FUNCTION___syscall3(SYS_write, 1, s, len);
}

uint32_t my_read(uint8_t *s, uint32_t maxlen) {
    int i=0;
    while (i < maxlen) {
        // FUNCTION_my_syscall(SYS_read, 0, s, 1);
        FUNCTION___syscall3(SYS_read, 0, s, 1);
        if (*s == '\x00' || *s == '\n') {
            return i;
        }
        i ++;
        s ++;
    }
}

void my_srand(uint32_t seed) {
    S_rand_seed = seed;
}

uint32_t my_rand() {
    uint32_t val = ((S_rand_seed * 1103515245) + 12345) & 0x7fffffff;
    S_rand_seed = val;
    return val;
}

void my_exit(uint32_t code) {
    // FUNCTION_my_syscall(SYS_exit_group, code);
    FUNCTION_tiny_exit(code);
}

char *my_itoa(char *p, uint32_t x)
{
    
	// number of digits in a uint32_t + NUL
	p += 11;
	*--p = 0;
	do {
		*--p = '0' + x % 10;
		x /= 10;
	} while (x);
	return p;
}

uint32_t getcurrtime() {
    // return FUNCTION_my_syscall(SYS_time, 0, 0, 0);
    return FUNCTION___syscall3(SYS_time, 0, 0, 0);
}


int isdigit(int c)
{
	return (unsigned)c-'0' < 10;
}

int isspace(int c)
{
	return c == ' ' || (unsigned)c-'\t' < 5;
}

int my_atoi(const char *s)
{
	int n=0, neg=0;
	while (FUNCTION_isspace(*s)) s++;
	switch (*s) {
	case '-': neg=1;
	case '+': s++;
	}
	/* Compute n as a negative number to avoid overflow on INT_MIN */
	while (FUNCTION_isdigit(*s))
		n = 10*n - (*s++ - '0');
	return neg ? n : -n;
}

int my_readint() {
    char buff[30];
    FUNCTION_my_read(buff, 20);
    return FUNCTION_my_atoi(buff);
}





/************************************************************************

re_chall.c

*/

#include <unistd.h>
#include <sys/syscall.h>   /* For SYS_xxx definitions */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


// #define RE_CHALL_DEBUG

#define GAMEBOARD_HEIGHT 4
#define GAMEBOARD_LENGTH 4
typedef uint16_t gamboard_type;
gamboard_type gameboard[GAMEBOARD_HEIGHT+2];
uint64_t game_score = 0;

int is_admin = 0;


#ifdef RE_CHALL_DEBUG

void showstate(uint32_t l) {
    for (uint32_t j=0; j<GAMEBOARD_LENGTH; j++) {
        printf("|");
        for (uint32_t k=0; k<GAMEBOARD_LENGTH; k++) {
            if ((l & (1 << (j*GAMEBOARD_LENGTH+k))) != 0) {
                // printf("%llx- ", l & (1 << (j*GAMEBOARD_LENGTH+k)));
                printf("1 ");
            } else {
                printf("0 ");
            }
        }
        printf("|\n");
    }
}

void showgameboard() {
    for (int i=0; i<GAMEBOARD_HEIGHT+1; i++) {
        gamboard_type l = S_gameboard[i];
        printf("---------\n");
        showstate(l);
        printf("---------\n\n");
    }
}
#endif

#define Y1 1
#define Y2 (1<<4)
#define Y4 (1<<8)
#define Y8 (1<<12)

const gamboard_type y2borad[16] = {0, Y1, Y2, Y1|Y2, Y4, Y4|Y1, Y4|Y2, Y4|Y2|Y1, Y8, Y8|Y1, Y8|Y2, Y8|Y2|Y1, Y8|Y4, Y8|Y4|Y1, Y8|Y4|Y2, Y8|Y4|Y2|Y1};

gamboard_type gen_res(uint32_t x, uint32_t y, uint32_t pos_x, uint32_t pos_y) {
    uint32_t res = 0;
    res |= (x << (4*pos_x));
    res |= S_y2borad[y] << pos_y;
    return res;
}

gamboard_type gen_model() {
    uint32_t tmp = FUNCTION_my_rand();
    uint32_t x = (tmp) & 0xF;
    uint32_t y = (tmp >> 4) & 0xF;
    uint32_t pos = (tmp >> 8) & 0xF;
    uint32_t pos_x = pos & 0x3;
    uint32_t pos_y = (pos >> 2) & 0x3;

    

    #ifdef RE_CHALL_DEBUG
    printf("curr_model: 0x%x; x: 0x%x; y: 0x%x; pos_x: 0x%x; pos_y: 0x%x; \n", tmp&0xFFFF, x, y, pos_x, pos_y);
    // showstate(9);
    // printf("debug: 0x%x\n", (x << (4*pos_x)));
    printf(S_asc_0);
    #endif

    return FUNCTION_gen_res(x, y, pos_x, pos_y);
}

#define MASK ((1 << 0x10)-1)

// Rotate x
gamboard_type rox(gamboard_type in) {
    gamboard_type res = (in << 4) & MASK;
    res |= (in >> (4*3));
    return res;
}

gamboard_type roy(gamboard_type in) {
    gamboard_type res = ((in << 1) & 0xEEEE) | ((in >> 3) & 0x1111);
    // printf("0x%x 0x%x\n", in, ((in >> 3) & 0x1111));
    return res;
}

#define XF 0xF
#define YF Y8|Y4|Y2|Y1

void eliminate_line(uint32_t level, gamboard_type curr_checker) {
    for (int i=level; i>0; i--) {
        // S_gameboard[i] = S_gameboard[i] ^ curr_checker;
        S_gameboard[i] = S_gameboard[i] & (~curr_checker);
        S_gameboard[i] |= (S_gameboard[i-1] & curr_checker);
    }
}

// check level1

uint32_t eliminate_block() {
    uint32_t level = GAMEBOARD_HEIGHT;
    register gamboard_type curr_checker;
    while (level > 0) {
        uint32_t f = 0;
        gamboard_type currboard = S_gameboard[level];
        for (int i=0; i<4; i++) {
            curr_checker = XF << (i*4);
            // printf("XF: %x\n", curr_checker);
            if ((currboard & curr_checker) == curr_checker) {
                f = 1;
                S_game_score ++;
                FUNCTION_eliminate_line(level, curr_checker);
                currboard = S_gameboard[level];
                // FUNCTION_my_puts(S_asc_1);
            }
        }
        for (int i=0; i<4; i++) {
            curr_checker = (YF) << i;
            // printf("YF: %x\n", curr_checker);
            if ((currboard & curr_checker) == curr_checker) {
                f = 1;
                S_game_score++;
                FUNCTION_eliminate_line(level, curr_checker);
                currboard = S_gameboard[level];
                // FUNCTION_my_puts(S_asc_1);
            }
        }

        if (f == 0) {
            level --;
        }
    }
    return 0;
}

gamboard_type transform_model(gamboard_type curr_model, uint32_t curr_mov) {
    int xx=0, yy=0;
    char buf[10];
    for (int i=0; i<4; i++) {
        if ((curr_mov >> (i+4)) & 1) {
            curr_model = FUNCTION_rox(curr_model);
            xx ++;
        }
        // curr_mov = curr_mov >> 1;
        // FUNCTION_my_puts(S_asc_1);
        // FUNCTION_my_puts(S_asc_0);
        // FUNCTION_admin_showgameboard();
        // FUNCTION_my_puts(S_asc_0);
    }
    for (int i=0; i<4; i++) {
        if ((curr_mov >> (i)) & 1) {
            curr_model = FUNCTION_roy(curr_model);
            yy ++;
        }
        // curr_mov = curr_mov >> 1;
        // FUNCTION_my_puts(S_asc_1);
        // FUNCTION_my_puts(S_asc_0);
        // FUNCTION_admin_showgameboard();
        // FUNCTION_my_puts(S_asc_0);
    }
    // if (curr_mov == 1) {
    //     curr_model = FUNCTION_rox(curr_model);
    // } else {
    //     curr_model = FUNCTION_roy(curr_model);
    // }
    #ifndef __RELEASE__
    register char *p = FUNCTION_my_itoa(buf, xx);
    FUNCTION_my_puts(p);
    p = FUNCTION_my_itoa(buf, yy);
    FUNCTION_my_puts(p);
    #endif
    return curr_model;
}

void append_model_to_gameboard(gamboard_type curr_model) {
    int i=0;
    for (i=0; i<GAMEBOARD_HEIGHT; i++) {
        if (S_gameboard[i+1] & curr_model) {
            S_gameboard[i] |= curr_model;
            break;
        }
    }
    if (i == GAMEBOARD_HEIGHT) {
        S_gameboard[i] |= curr_model;
    }
}

void check_dead() {
    if (S_gameboard[0]) {
        FUNCTION_my_puts(S_aYouLose);
        FUNCTION_my_exit(0);
    }
}

int check_win() {
    if (S_game_score > 150) {
        return 1;
    } else {
        return 0;
    }
}

uint32_t goooo(uint8_t movs, gamboard_type model) {
    gamboard_type curr_model = model;
    int i=0;

    // for (i=0; i<GAMEBOARD_HEIGHT; i++) {
        // uint32_t curr_mov = movs & 3;
        // movs = movs >> 2;

        // #ifdef RE_CHALL_DEBUG
        // showstate(curr_model);
        // showgameboard();
        // puts(S_aInput);
        // scanf("%d", &curr_mov);
        // #endif

        // if (curr_mov & 2) {
        //     break;
        // }

    //     curr_model = FUNCTION_transform_model(curr_model, curr_mov);
    // }

    #ifndef __RELEASE__
    // FUNCTION_my_puts(S_asc_1);
    // FUNCTION_admin_showstate(model);
    // FUNCTION_my_puts(S_asc_0);
    // FUNCTION_admin_showgameboard();
    // FUNCTION_my_puts(S_asc_0);
    #endif
        

    curr_model = FUNCTION_transform_model(curr_model, movs);

    FUNCTION_append_model_to_gameboard(curr_model);
    FUNCTION_check_dead();
    FUNCTION_eliminate_block();

    
    return 0;
}

uint32_t play(uint8_t *input_str, uint32_t input_str_len) {
    #ifdef RE_CHALL_DEBUG
    printf("len: ");
    scanf("%d", &input_str_len);
    #endif
    char score_buf[20];
    for (int i=0; i<input_str_len; i++) {   
        if (FUNCTION_check_win() == 1) {
            return 0;
        }  
        #ifndef __RELEASE__           
        FUNCTION_my_puts(S_aScore);
        register char *p = FUNCTION_my_itoa(score_buf, S_game_score);
        FUNCTION_my_puts(p);
        
        FUNCTION_my_puts(S_asc_0);
        #endif

        uint32_t movs = input_str[i];
        gamboard_type model = FUNCTION_gen_model();
        FUNCTION_goooo(movs, model);
    }
    return 0;
}

void my_init() {
    uint32_t ttt = FUNCTION_getcurrtime();
    // printf("time: 0x%x\n", ttt);
    uint8_t buff[20];
    FUNCTION_my_puts(S_aTimestamp);
    register char *p = FUNCTION_my_itoa(buff, ttt);
    FUNCTION_my_puts(buff);
    FUNCTION_my_puts(S_asc_0);
    FUNCTION_my_srand(ttt);
}

int game() {
    FUNCTION_my_init();
    FUNCTION_my_puts(S_aInput);
    uint8_t input_str[1008];

    // FUNCTION_my_syscall(SYS_read, 0, input_str, 30);
    FUNCTION_my_read(input_str, 1000);

    register int len = FUNCTION_my_strlen(input_str);
    FUNCTION_play(input_str, len);

    return FUNCTION_check_win();
}

void game_main() {
    if (FUNCTION_game()) {
        FUNCTION_my_puts(S_aCongratulation);
        S_is_admin = 1;
    } else {
        FUNCTION_my_puts(S_aFail);
    }
}



/************************************************************************

admin.c

*/


heap_t gv_heap;
bin_t heap_bins[BIN_COUNT];

void admin_menu() {
    FUNCTION_my_puts(S_asc_1);
    FUNCTION_my_puts(S_aAdminMenu);
    FUNCTION_my_puts(S_a1New);
    FUNCTION_my_puts(S_a2Edit);
    FUNCTION_my_puts(S_a3Show);
    FUNCTION_my_puts(S_a4Free);
    FUNCTION_my_puts(S_a5AdminSGame);
    FUNCTION_my_puts(S_a6AdminSLounge);
    FUNCTION_my_puts(S_a8DisableDynloa);
    FUNCTION_my_puts(S_a999Return);
    FUNCTION_my_puts(S_asc_2);
    FUNCTION_my_puts(S_aChoice);
}

void admin_showstate(uint32_t l) {
    for (uint32_t j=0; j<GAMEBOARD_LENGTH; j++) {
        FUNCTION_my_puts(S_asc_3);
        for (uint32_t k=0; k<GAMEBOARD_LENGTH; k++) {
            if ((l & (1 << (j*GAMEBOARD_LENGTH+k))) != 0) {
                FUNCTION_my_puts(S_a1);
            } else {
                FUNCTION_my_puts(S_a0);
            }
        }
        FUNCTION_my_puts(S_asc_3);
        FUNCTION_my_puts(S_asc_0);
    }
}

void admin_showgameboard() {
    for (int i=0; i<GAMEBOARD_HEIGHT+1; i++) {
        gamboard_type l = S_gameboard[i];
        FUNCTION_my_puts(S_asc_4);
        FUNCTION_admin_showstate(l);
        FUNCTION_my_puts(S_asc_5);
    }
}

void admin_game() {
    for (int i=0; i<GAMEBOARD_LENGTH+2; i++) {
        S_gameboard[i] = 0;
    }
    S_game_score = 0;

    char score_buf[20];
    while (1) {
        FUNCTION_my_puts(S_asc_0);
        FUNCTION_my_puts(S_aScore);
        register char *p = FUNCTION_my_itoa(score_buf, S_game_score);
        FUNCTION_my_puts(p);
        FUNCTION_my_puts(S_asc_0);

        gamboard_type model = FUNCTION_gen_model();
        FUNCTION_admin_showstate(model);

        FUNCTION_my_puts(S_asc_0);
        FUNCTION_admin_showgameboard();
        FUNCTION_my_puts(S_asc_0);

        char movs[20];
        FUNCTION_my_read(movs, 10);
        if (movs[1] == 'Q' || movs[1] == 'q') {
            break;
        }
        FUNCTION_goooo(movs[0], model);
    }
}

void admin_set_seed() {
    FUNCTION_my_puts(S_aYouCheatCodePl);
    register uint32_t tmp = FUNCTION_my_readint();
    FUNCTION_my_srand(tmp);
}


char *ptr[16];
int ptr_size[16];

void *my_heap_alloc(int size) {
    register void * tmp = FUNCTION_heap_alloc(&S_gv_heap, size);
    
    // char buf[20];
    // register char *p = FUNCTION_my_itoa(buf, tmp);
    // FUNCTION_my_puts(p);
    // FUNCTION_my_puts(S_asc_0);

    return tmp;
}

void my_heap_free(void *p) {
    // char buf[20];
    // register char *pp = FUNCTION_my_itoa(buf, p);
    // FUNCTION_my_puts(pp);
    // FUNCTION_my_puts(S_asc_0);

    FUNCTION_heap_free(&S_gv_heap, p);
}

void show()
{
	FUNCTION_my_puts(S_aIndex);
    int index = FUNCTION_my_readint();
    if(index >= 0 && index < 16 && S_ptr[index]) {
        FUNCTION_my_puts(S_ptr[index]);
    } else {
        return;
    }
}
void edit()
{
	FUNCTION_my_puts(S_aIndex);
    int index = FUNCTION_my_readint();
	FUNCTION_my_puts(S_aSize);
	int size = FUNCTION_my_readint();
    if(index >= 0 && index < 16 && S_ptr[index] && size <= S_ptr_size[index]) {
        // FUNCTION_my_read(S_ptr[index], size);
        // FUNCTION___syscall3(SYS_read, 0, S_ptr[index], size);
        FUNCTION_tiny_read(0, S_ptr[index], size);
        FUNCTION_tiny_write(1, S_ptr[index], size);
    } else {
        return;
    }
}
void allocate()
{
	// int padding[30];		// for one gadget
	// memset(padding, 0, sizeof(padding));	
	int i;
	for (i = 0; i < 0x10; i++) {
        if (S_ptr[i] == 0)
            break;
    }
    if (i >= 0x10) {
        FUNCTION_my_puts(S_aNoMoreChunk);
        return;
    }
    FUNCTION_my_puts(S_aSize);
    int size = FUNCTION_my_readint();
    if (size > 0x1000) return;
    S_ptr[i] = FUNCTION_my_heap_alloc(size);
    S_ptr_size[i] = size;
}
void delete()
{
	FUNCTION_my_puts(S_aIndex);
    int index = FUNCTION_my_readint();
    if(index >= 0 && index < 16 && S_ptr[index]) {
        FUNCTION_my_heap_free(S_ptr[index]);
        S_ptr[index] = 0;
        S_ptr_size[index] = 0;
    } else {
        return;
    }
}

void heap_init() {
    // void *region = malloc(HEAP_INIT_SIZE);
    void *region = FUNCTION_tiny_mmap(0, HEAP_INIT_SIZE, PROT_READ|PROT_WRITE, MAP_ANONYMOUS|MAP_PRIVATE, -1, 0);
    if(region == -1)
    {
        FUNCTION_my_puts(S_aMmapError);
        FUNCTION_my_exit(-1);
    }
    for (int i = 0; i < BIN_COUNT; i++) {
        S_gv_heap.bins[i] = &(S_heap_bins[i]);
        // memset(heap->bins[i], 0, sizeof(bin_t));
    }
    FUNCTION_init_heap(&S_gv_heap, region);
}

typedef struct{
    void *mmap_addr;
    size_t mmap_size;
    unsigned char* id;
    unsigned char* hex_id;
}func_block_st__;


#define SHELLCODE_NUM 87
#define SC_NAME_LEN 40
const uint8_t sc_name[SHELLCODE_NUM][SC_NAME_LEN] = {
    "a43122d57b04677ca042b3936387448f",
"733ec491a44280ae733a9fea8d60d328",
"a351539ea701278daf0376b0854150a8",
"b69d0733f0d45a2c677d00446b1ddbd9",
"c3565ac45dff9848dac7ac4c223e6c61",
"8f9a4351cb07aea3550cbdeee41d1dc5",
"43572e512407331635d42fecccfc4b90",
"b901ba71fddf5d7125031eb89f1829ad",
"9c60e5982025fc013a164109fd5da8a0",
"4252c9ab061ec394775dee239c311b99",
"32529c5fac4bd13fd80ce4779bc09f56",
"ef32d4f3a5a9c31732a062e18cb83f17",
"97f7a7dfae6b5322af928b4632c6245c",
"384aabf74045dbd102fcf7abf2f067d6",
"f94bf8bc09378d2f7685a54cbf3941ce",
"95b8db612678398cd2577fc64676fe92",
"2eac2ac04823230417cdd35afe2a924e",
"83deb0177b035c1530529443801b3fc4",
"93446c33d25b35ed390f2a8b9a5ea6a4",
"1ee3b21edb88d9a3185690f021d94fa1",
"62e9418f31fac6ed6c736fa0fc47334c",
"2d725268ae170f36d65ca2c69b5fea31",
"7abda925d9136b5c5c382429440a07ed",
"c0ea89643e4324d75177370b3db94535",
"b0b68c5b3c9a52cfe072fd15b8437bb6",
"8faae97b2c3830dddaf06f50b8bae7b6",
"d8ecc9210b3d09343275867753028433",
"2aabc9ada0855def47eba259d9020d52",
"2b438a4058cb3aa000bf20f133c51c75",
"aa899f2e58de2466e0e2ccdbbcb5b693",
"f464264900c0a3519a11a39dc17d83c2",
"8fbca1bd592437c824b0990271527da1",
"f40f375263a5a4b078473cadc2746631",
"f018622565f4d85326122027e5bff1a5",
"508e799d314a8da19f966ca4936db71c",
"30cfeac00d70d975707889bcc2f53614",
"79e908c9a12f9967a29d5be3e15bdb29",
"c05e47ecac8145772622412db0bb039e",
"c7d66329b9e4428c8805c6d450bc9f8a",
"188db852f6f3d80d36827185ec74a052",
"b7679436c55a717ca2f2576f096e6084",
"90c588d11ce8422619c08eaaaf858c8b",
"b9496737e1ed90fcd78b3be3806a7344",
"632a2fa60bed84ae2a77d6bfbf6159dc",
"31a8b2bbee5727f68282385e41119172",
"3ab0ab6471f17f872b75a4da8235765b",
"34ce68911ae2209b5eb82a272b56cdb3",
"c8ec4eba51c1a351c5d526b1175e2455",
"92e99fe82dd7f91fa63c479d584b95ad",
"2eef166f46bca4162fab0bf36f0e54d2",
"79958b70ca059fb7e4eb80f064035b80",
"3e11029d5ac2211c31bdae5124c9795a",
"30e23ac2f4b46087f0a0d2cb92a5de4f",
"e40365731e828164ae4153f8cc3c7dc7",
"6adf580f39636131583b54beeb6a9e9b",
"a113ccb9afe3d088a759f418a58555ea",
"5f66dd0c765a66986c7ceb1acffb1371",
"957fd0e74de00cde1c7d052bd68b4a64",
"41c24acbb388171678325e74b5837664",
"d7075998ed4eb4e6c0d8692c05d08f6b",
"0bd3c50f774fd998f9c6c816fa0a491b",
"b8f1ef9d5ae177738dae64e46bccb3d1",
"7ff27b3009a6724e417577fa4637469b",
"2dc45082caf29e32af19b002e24878fb",
"e062ddf3fd4192ea556cc284d824a418",
"0328d2301fb084d3aafcc60988b9115e",
"e963106043f784fe28c906a769d6ca66",
"346496bdc50defbe155f22689b03fd2c",
"ecd6414a6922910a52401cc4368c9386",
"2f4fd98d72c3e137be0f387dcda8a680",
"759d259a1c44869f437687b18c97077a",
"e4f2b3b04ee744a2c49c912735d79d80",
"9133d30e17d794fc9d6dceb616731f60",
"48f11c9227eec580445b20ef26456a0b",
"704ad7cfad24606684348d8b5ea4ea6f",
"e138c675a1cf000b2e664483c5eaa2d4",
"b33a34b13be73f57ffce243076d9f2da",
"abbf69349811d17b6edaba15464ac6f6",
"3445b01dfb9386195e8e3a07d49a3867",
"2184489db56112d2c0d8b7536abb075f",
"79482f2d1a19a683aa67b0e811f8f8bc",
"7e697c09cb0fcb076e2c59ddf9adb741",
"5d8e3f065e0567b793b94e97a6633be6",
"06b9d99befb919c2d9733cbf17b5d07a",
"9e6c47893f0b949110f9c3a19e7e436f",
"0079eec473e879003b562b3e6fcefa00",
"6e88d889ecde3b574e5514c14d620a19",
};
func_block_st__ *sc_addr[SHELLCODE_NUM];


void unmap_all() {
    for (int i=0; i<SHELLCODE_NUM; i++) {
        if (S_sc_addr[i] != 0) {
            FUNCTION_tiny_munmap(S_sc_addr[i]->mmap_addr, 0x2000);
            FUNCTION_my_heap_free(S_sc_addr[i]->id);
            // FUNCTION_my_heap_free(S_sc_addr[i]->hex_id);
            FUNCTION_my_heap_free(S_sc_addr[i]);
            S_sc_addr[i] = 0;
        }
    }
}

void clean1(func_block_st__* curr) {
    FUNCTION_my_heap_free(curr->id);
    FUNCTION_my_heap_free(curr);
}

void clean2(func_block_st__* curr) {
    FUNCTION_my_heap_free(curr);
}

void map_all_file() {
    FUNCTION_unmap_all();
    for (int i=0; i<SHELLCODE_NUM; i++) {
        func_block_st__* curr = FUNCTION_my_heap_alloc(sizeof(func_block_st__)); // 32 
        curr->id = FUNCTION_my_heap_alloc(40);
        // curr->hex_id = FUNCTION_my_heap_alloc(40);
        
        int fd = -1;

        uint32_t addr = FUNCTION_my_rand() & 0xfffff000;
        while (addr <= 0x10000000) {
            addr = FUNCTION_my_rand() & 0xfffff000;
        }

        
        #ifdef RODATA_PROXY
        if((fd = FUNCTION_tiny_open(S_sc_name, O_RDONLY)) < 0){
        #else
        if((fd = FUNCTION_tiny_open(S_sc_name[i], O_RDONLY)) < 0){
        #endif
            FUNCTION_my_puts(S_aOpenError); 
            FUNCTION_my_puts(S_sc_name[i]);
            FUNCTION_my_puts(S_asc_0);
            FUNCTION_my_exit(0);
        }
        void *mapped = 0;
        if((mapped = FUNCTION_tiny_mmap((void *)addr, 0x2000, PROT_READ|PROT_EXEC, MAP_SHARED, fd, 0)) ==(void*) -1){
            FUNCTION_my_puts(S_aMmapError);
            FUNCTION_my_exit(0);
        }
        FUNCTION_tiny_close(fd);
        // FUNCTION_my_puts("OK\n");
        
        if (mapped == (void *)addr) {
            curr->mmap_addr = mapped;
            curr->mmap_size = 0x2000;
            #ifdef RODATA_PROXY
            FUNCTION_my_strcpy(curr->id, S_sc_name);
            #else
            FUNCTION_my_strcpy(curr->id, S_sc_name[i]);
            #endif
            S_sc_addr[i] = curr;
        } else {
            // Error!
            
            FUNCTION_clean1(curr);
            
            FUNCTION_clean2(curr);
            return;
        }
    }

    FUNCTION_my_puts(S_aDynloadDisable);
    return;
}

void admin_handler() {
    if (S_is_admin != 1) {
        FUNCTION_my_puts(S_aPleaseLoginFir);
        return;
    }
    
    if (S_gv_heap.start == 0) {
        FUNCTION_heap_init();
    }
    while (1) {
        FUNCTION_admin_menu();
        int choice = FUNCTION_my_readint();
        switch (choice) {
            case 1:
                FUNCTION_allocate();
                break;
            case 2:
                FUNCTION_edit();
                break;
            case 3:
                FUNCTION_show();
                break;
            case 4:
                FUNCTION_delete();
                break;
            case 5:
                FUNCTION_admin_game();
                break;
            case 6:
                FUNCTION_admin_set_seed();
                break;
            case 7:
                FUNCTION_map_all_file();
                break;
            case 999:
                return;
                break;
            default:
                FUNCTION_my_puts(S_aUnknowOption);
                // FUNCTION_my_exit(0);
        }
    }
}



/************************************************************************

main.c

*/

#ifndef __RELEASE__
#define MAIN_DEBUG
#endif

void welcome() {
    // FUNCTION_my_puts(    "###############################################################\n"
    //             " #                                                             #\n"
    //             "  #      #######      #         ######      #      ####         #\n"
    //             "   #      #           # #        ##         ##      #   #        #\n"
    //             "    #      ######     #   #       ######      #      ####         #\n"
    //             "     #      #         # ### #          ##      #      #  #         #\n"
    //             "      #      #        #       #     ######    #####    #   #        #\n"
    //             "       #                                                             #\n"
    //             "        ###############################################################\n\n\n"
    //         );
    FUNCTION_my_puts(S_asc_6);
}

void menu() {
    FUNCTION_my_puts(S_asc_1);
    FUNCTION_my_puts(S_a1Login);
    FUNCTION_my_puts(S_a2Getflag);
    FUNCTION_my_puts(S_a3AdminSMenu);
    FUNCTION_my_puts(S_a4GetAdminSPass);
    FUNCTION_my_puts(S_a9Help);
    FUNCTION_my_puts(S_a0Exit);
    FUNCTION_my_puts(S_asc_2);
    FUNCTION_my_puts(S_aChoice);
}

void getflag_handler() {
    if (S_is_admin == 1) {
        int fd = FUNCTION_tiny_open(S_aFlag, O_RDONLY);
        if (fd < 0) {
            return;
        }
        char buff[100];
        FUNCTION_tiny_read(fd, buff, 100);
        FUNCTION_my_puts(buff);
        FUNCTION_my_puts(S_asc_0);
        FUNCTION_tiny_close(fd);
    } else {
        FUNCTION_my_puts(S_aPleaseLoginFir);
    }
}

void get_admin_functions() {
    if (S_is_admin == 1) {
        int fd = FUNCTION_tiny_open(S_aHomePwnAdminPw, O_RDONLY);
        if (fd < 0) {
            return;
        }
        char buff[100];
        FUNCTION_tiny_read(fd, buff, 100);
        FUNCTION_my_puts(buff);
        FUNCTION_my_puts(S_asc_0);
        FUNCTION_tiny_close(fd);
    } else {
        FUNCTION_my_puts(S_aPleaseLoginFir);
    }
}

void help() {
    FUNCTION_my_puts(S_aHelp);
    FUNCTION_my_puts(S_a1LoginChalleng);
    FUNCTION_my_puts(S_a2GetflagOnlyAd);
    FUNCTION_my_puts(S_a3AdminSMenu);
    FUNCTION_my_puts(S_a4PasswordForDe);
    FUNCTION_my_puts(S_a9Help);
    FUNCTION_my_puts(S_a0Exit);
    FUNCTION_my_puts(S_asc_0);
}

void admin_handler();


void main() {
    FUNCTION_welcome();

    while (1) {
        FUNCTION_menu();
        int choice = FUNCTION_my_readint();
        switch (choice) {
            case 1:
                FUNCTION_game_main();
                break;
            case 2:
                FUNCTION_getflag_handler();
                break;
            case 3:
                FUNCTION_admin_handler();
                break;
            case 4:
                FUNCTION_get_admin_functions();
                break;
            case 9:
                FUNCTION_help();
                break;
            case 999:
                FUNCTION_my_puts(S_aBye);
                // FUNCTION_my_exit(0);
                return;
                break;
            #ifdef MAIN_DEBUG
            case 666:
                S_is_admin = 1;
                break;
            #endif
            default:
                FUNCTION_my_puts(S_aUnknowOption);
                // FUNCTION_my_puts(S_aUnknowOption);
                // FUNCTION_my_puts(PROXY_aUnknowOption+RODATA_BASE);
                FUNCTION_my_exit(0);
        }
    }
}
