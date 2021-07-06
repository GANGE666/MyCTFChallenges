#define FUNCTION_PROXY
#include <immintrin.h>

#define FUNCTION_ARG0()    ((uint64_t (*)())(*(void **)(0x300000)))()
#define FUNCTION_ARG1(arg1)    ((uint64_t (*)(void *))(*(void **)(0x300000)))(arg1)
#define FUNCTION_ARG2(arg1, arg2)    ((uint64_t (*)(void *, void *))(*(void **)(0x300000)))(arg1, arg2)
#define FUNCTION_ARG3(arg1, arg2, arg3)    ((uint64_t (*)(void *, void *, void *))(*(void **)(0x300000)))(arg1, arg2, arg3)
#define FUNCTION_ARG4(arg1, arg2, arg3, arg4)    ((uint64_t (*)(void *, void *, void *, void *))(*(void **)(0x300000)))(arg1, arg2, arg3, arg4)
#define FUNCTION_ARG5(arg1, arg2, arg3, arg4, arg5)    ((uint64_t (*)(void *, void *, void *, void *, void *))(*(void **)(0x300000)))(arg1, arg2, arg3, arg4, arg5)
#define FUNCTION_ARG6(arg1, arg2, arg3, arg4, arg5, arg6)    ((uint64_t (*)(void *, void *, void *, void *, void *, void *))(*(void **)(0x300000)))(arg1, arg2, arg3, arg4, arg5, arg6)
#define FUNCTION_ARG7(arg1, arg2, arg3, arg4, arg5, arg6, arg7)    ((uint64_t (*)(void *, void *, void *, void *, void *, void *, void *))(*(void **)(0x300000)))(arg1, arg2, arg3, arg4, arg5, arg6, arg7)



#define FUNCTION_TEMP(arg1) ({ \
register __m128i exid_in_x123456 asm("xmm15"); \
exid_in_x123456 = _mm_set_epi8(0x9e, 0x6c, 0x47, 0x89, 0x3f, 0xb, 0x94, 0x91, 0x10, 0xf9, 0xc3, 0xa1, 0x9e, 0x7e, 0x43, 0x6f); \
((void (*)(char *))(*(void **)(0x300000)))(arg1); \
})


#ifdef FUNCTION_PROXY
#define FUNCTION_get_admin_functions() ({ \
register __m128i exid_in_get_admin_functions asm("xmm15"); \
exid_in_get_admin_functions = _mm_set_epi8(0xe6, 0x3b, 0x63, 0xa6, 0x97, 0x4e, 0xb9, 0x93, 0xb7, 0x67, 0x5, 0x5e, 0x6, 0x3f, 0x8e, 0x5d); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_get_admin_functions  get_admin_functions
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_admin_game() ({ \
register __m128i exid_in_admin_game asm("xmm15"); \
exid_in_admin_game = _mm_set_epi8(0x5e, 0x11, 0xb9, 0x88, 0x9, 0xc6, 0xfc, 0xaa, 0xd3, 0x84, 0xb0, 0x1f, 0x30, 0xd2, 0x28, 0x3); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_admin_game  admin_game
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_admin_set_seed() ({ \
register __m128i exid_in_admin_set_seed asm("xmm15"); \
exid_in_admin_set_seed = _mm_set_epi8(0x66, 0xca, 0xd6, 0x69, 0xa7, 0x6, 0xc9, 0x28, 0xfe, 0x84, 0xf7, 0x43, 0x60, 0x10, 0x63, 0xe9); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_admin_set_seed  admin_set_seed
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_clean1(arg0) ({ \
register __m128i exid_in_clean1 asm("xmm15"); \
exid_in_clean1 = _mm_set_epi8(0xd4, 0xa2, 0xea, 0xc5, 0x83, 0x44, 0x66, 0x2e, 0xb, 0x0, 0xcf, 0xa1, 0x75, 0xc6, 0x38, 0xe1); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_clean1  clean1
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_clean2(arg0) ({ \
register __m128i exid_in_clean2 asm("xmm15"); \
exid_in_clean2 = _mm_set_epi8(0xda, 0xf2, 0xd9, 0x76, 0x30, 0x24, 0xce, 0xff, 0x57, 0x3f, 0xe7, 0x3b, 0xb1, 0x34, 0x3a, 0xb3); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_clean2  clean2
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_admin_showstate(arg0) ({ \
register __m128i exid_in_admin_showstate asm("xmm15"); \
exid_in_admin_showstate = _mm_set_epi8(0xfb, 0x78, 0x48, 0xe2, 0x2, 0xb0, 0x19, 0xaf, 0x32, 0x9e, 0xf2, 0xca, 0x82, 0x50, 0xc4, 0x2d); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_admin_showstate  admin_showstate
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_admin_showgameboard() ({ \
register __m128i exid_in_admin_showgameboard asm("xmm15"); \
exid_in_admin_showgameboard = _mm_set_epi8(0x18, 0xa4, 0x24, 0xd8, 0x84, 0xc2, 0x6c, 0x55, 0xea, 0x92, 0x41, 0xfd, 0xf3, 0xdd, 0x62, 0xe0); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_admin_showgameboard  admin_showgameboard
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION__start(arg0, arg1) ({ \
register __m128i exid_in__start asm("xmm15"); \
exid_in__start = _mm_set_epi8(0x8f, 0x44, 0x87, 0x63, 0x93, 0xb3, 0x42, 0xa0, 0x7c, 0x67, 0x4, 0x7b, 0xd5, 0x22, 0x31, 0xa4); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION__start  _start
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_deregister_tm_clones() ({ \
register __m128i exid_in_deregister_tm_clones asm("xmm15"); \
exid_in_deregister_tm_clones = _mm_set_epi8(0x28, 0xd3, 0x60, 0x8d, 0xea, 0x9f, 0x3a, 0x73, 0xae, 0x80, 0x42, 0xa4, 0x91, 0xc4, 0x3e, 0x73); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_deregister_tm_clones  deregister_tm_clones
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_register_tm_clones() ({ \
register __m128i exid_in_register_tm_clones asm("xmm15"); \
exid_in_register_tm_clones = _mm_set_epi8(0xa8, 0x50, 0x41, 0x85, 0xb0, 0x76, 0x3, 0xaf, 0x8d, 0x27, 0x1, 0xa7, 0x9e, 0x53, 0x51, 0xa3); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_register_tm_clones  register_tm_clones
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION___do_global_dtors_aux() ({ \
register __m128i exid_in___do_global_dtors_aux asm("xmm15"); \
exid_in___do_global_dtors_aux = _mm_set_epi8(0xd9, 0xdb, 0x1d, 0x6b, 0x44, 0x0, 0x7d, 0x67, 0x2c, 0x5a, 0xd4, 0xf0, 0x33, 0x7, 0x9d, 0xb6); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION___do_global_dtors_aux  __do_global_dtors_aux
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_frame_dummy() ({ \
register __m128i exid_in_frame_dummy asm("xmm15"); \
exid_in_frame_dummy = _mm_set_epi8(0x61, 0x6c, 0x3e, 0x22, 0x4c, 0xac, 0xc7, 0xda, 0x48, 0x98, 0xff, 0x5d, 0xc4, 0x5a, 0x56, 0xc3); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_frame_dummy  frame_dummy
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_add_node(arg0, arg1) ({ \
register __m128i exid_in_add_node asm("xmm15"); \
exid_in_add_node = _mm_set_epi8(0xc5, 0x1d, 0x1d, 0xe4, 0xee, 0xbd, 0xc, 0x55, 0xa3, 0xae, 0x7, 0xcb, 0x51, 0x43, 0x9a, 0x8f); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_add_node  add_node
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_remove_node(arg0, arg1) ({ \
register __m128i exid_in_remove_node asm("xmm15"); \
exid_in_remove_node = _mm_set_epi8(0x90, 0x4b, 0xfc, 0xcc, 0xec, 0x2f, 0xd4, 0x35, 0x16, 0x33, 0x7, 0x24, 0x51, 0x2e, 0x57, 0x43); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_remove_node  remove_node
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_get_best_fit(arg0, arg1) ({ \
register __m128i exid_in_get_best_fit asm("xmm15"); \
exid_in_get_best_fit = _mm_set_epi8(0xad, 0x29, 0x18, 0x9f, 0xb8, 0x1e, 0x3, 0x25, 0x71, 0x5d, 0xdf, 0xfd, 0x71, 0xba, 0x1, 0xb9); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_get_best_fit  get_best_fit
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_get_last_node(arg0) ({ \
register __m128i exid_in_get_last_node asm("xmm15"); \
exid_in_get_last_node = _mm_set_epi8(0xa0, 0xa8, 0x5d, 0xfd, 0x9, 0x41, 0x16, 0x3a, 0x1, 0xfc, 0x25, 0x20, 0x98, 0xe5, 0x60, 0x9c); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_get_last_node  get_last_node
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_init_heap(arg0, arg1) ({ \
register __m128i exid_in_init_heap asm("xmm15"); \
exid_in_init_heap = _mm_set_epi8(0x99, 0x1b, 0x31, 0x9c, 0x23, 0xee, 0x5d, 0x77, 0x94, 0xc3, 0x1e, 0x6, 0xab, 0xc9, 0x52, 0x42); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_init_heap  init_heap
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_heap_alloc(arg0, arg1) ({ \
register __m128i exid_in_heap_alloc asm("xmm15"); \
exid_in_heap_alloc = _mm_set_epi8(0x56, 0x9f, 0xc0, 0x9b, 0x77, 0xe4, 0xc, 0xd8, 0x3f, 0xd1, 0x4b, 0xac, 0x5f, 0x9c, 0x52, 0x32); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_heap_alloc  heap_alloc
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_heap_free(arg0, arg1) ({ \
register __m128i exid_in_heap_free asm("xmm15"); \
exid_in_heap_free = _mm_set_epi8(0x17, 0x3f, 0xb8, 0x8c, 0xe1, 0x62, 0xa0, 0x32, 0x17, 0xc3, 0xa9, 0xa5, 0xf3, 0xd4, 0x32, 0xef); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_heap_free  heap_free
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_expand(arg0, arg1) ({ \
register __m128i exid_in_expand asm("xmm15"); \
exid_in_expand = _mm_set_epi8(0x5c, 0x24, 0xc6, 0x32, 0x46, 0x8b, 0x92, 0xaf, 0x22, 0x53, 0x6b, 0xae, 0xdf, 0xa7, 0xf7, 0x97); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_expand  expand
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_contract(arg0, arg1) ({ \
register __m128i exid_in_contract asm("xmm15"); \
exid_in_contract = _mm_set_epi8(0xd6, 0x67, 0xf0, 0xf2, 0xab, 0xf7, 0xfc, 0x2, 0xd1, 0xdb, 0x45, 0x40, 0xf7, 0xab, 0x4a, 0x38); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_contract  contract
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_get_bin_index(arg0) ({ \
register __m128i exid_in_get_bin_index asm("xmm15"); \
exid_in_get_bin_index = _mm_set_epi8(0xce, 0x41, 0x39, 0xbf, 0x4c, 0xa5, 0x85, 0x76, 0x2f, 0x8d, 0x37, 0x9, 0xbc, 0xf8, 0x4b, 0xf9); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_get_bin_index  get_bin_index
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_create_foot(arg0) ({ \
register __m128i exid_in_create_foot asm("xmm15"); \
exid_in_create_foot = _mm_set_epi8(0x92, 0xfe, 0x76, 0x46, 0xc6, 0x7f, 0x57, 0xd2, 0x8c, 0x39, 0x78, 0x26, 0x61, 0xdb, 0xb8, 0x95); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_create_foot  create_foot
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_get_foot(arg0) ({ \
register __m128i exid_in_get_foot asm("xmm15"); \
exid_in_get_foot = _mm_set_epi8(0x4e, 0x92, 0x2a, 0xfe, 0x5a, 0xd3, 0xcd, 0x17, 0x4, 0x23, 0x23, 0x48, 0xc0, 0x2a, 0xac, 0x2e); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_get_foot  get_foot
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_get_wilderness(arg0) ({ \
register __m128i exid_in_get_wilderness asm("xmm15"); \
exid_in_get_wilderness = _mm_set_epi8(0xc4, 0x3f, 0x1b, 0x80, 0x43, 0x94, 0x52, 0x30, 0x15, 0x5c, 0x3, 0x7b, 0x17, 0xb0, 0xde, 0x83); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_get_wilderness  get_wilderness
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_syscall(arg0, ...) ({ \
register __m128i exid_in_my_syscall asm("xmm15"); \
exid_in_my_syscall = _mm_set_epi8(0xa5, 0xf1, 0xbf, 0xe5, 0x27, 0x20, 0x12, 0x26, 0x53, 0xd8, 0xf4, 0x65, 0x25, 0x62, 0x18, 0xf0); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_syscall  my_syscall
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_strlen(arg0) ({ \
register __m128i exid_in_my_strlen asm("xmm15"); \
exid_in_my_strlen = _mm_set_epi8(0x1c, 0xb7, 0x6d, 0x93, 0xa4, 0x6c, 0x96, 0x9f, 0xa1, 0x8d, 0x4a, 0x31, 0x9d, 0x79, 0x8e, 0x50); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_strlen  my_strlen
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_strcpy(arg0, arg1) ({ \
register __m128i exid_in_my_strcpy asm("xmm15"); \
exid_in_my_strcpy = _mm_set_epi8(0x14, 0x36, 0xf5, 0xc2, 0xbc, 0x89, 0x78, 0x70, 0x75, 0xd9, 0x70, 0xd, 0xc0, 0xea, 0xcf, 0x30); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_my_strcpy  my_strcpy
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_puts(arg0) ({ \
register __m128i exid_in_my_puts asm("xmm15"); \
exid_in_my_puts = _mm_set_epi8(0x29, 0xdb, 0x5b, 0xe1, 0xe3, 0x5b, 0x9d, 0xa2, 0x67, 0x99, 0x2f, 0xa1, 0xc9, 0x8, 0xe9, 0x79); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_puts  my_puts
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_read(arg0, arg1) ({ \
register __m128i exid_in_my_read asm("xmm15"); \
exid_in_my_read = _mm_set_epi8(0x9e, 0x3, 0xbb, 0xb0, 0x2d, 0x41, 0x22, 0x26, 0x77, 0x45, 0x81, 0xac, 0xec, 0x47, 0x5e, 0xc0); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_my_read  my_read
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_srand(arg0) ({ \
register __m128i exid_in_my_srand asm("xmm15"); \
exid_in_my_srand = _mm_set_epi8(0x8a, 0x9f, 0xbc, 0x50, 0xd4, 0xc6, 0x5, 0x88, 0x8c, 0x42, 0xe4, 0xb9, 0x29, 0x63, 0xd6, 0xc7); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_srand  my_srand
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_rand() ({ \
register __m128i exid_in_my_rand asm("xmm15"); \
exid_in_my_rand = _mm_set_epi8(0x52, 0xa0, 0x74, 0xec, 0x85, 0x71, 0x82, 0x36, 0xd, 0xd8, 0xf3, 0xf6, 0x52, 0xb8, 0x8d, 0x18); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_my_rand  my_rand
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_exit(arg0) ({ \
register __m128i exid_in_my_exit asm("xmm15"); \
exid_in_my_exit = _mm_set_epi8(0x84, 0x60, 0x6e, 0x9, 0x6f, 0x57, 0xf2, 0xa2, 0x7c, 0x71, 0x5a, 0xc5, 0x36, 0x94, 0x67, 0xb7); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_exit  my_exit
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_itoa(arg0, arg1) ({ \
register __m128i exid_in_my_itoa asm("xmm15"); \
exid_in_my_itoa = _mm_set_epi8(0x8b, 0x8c, 0x85, 0xaf, 0xaa, 0x8e, 0xc0, 0x19, 0x26, 0x42, 0xe8, 0x1c, 0xd1, 0x88, 0xc5, 0x90); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_my_itoa  my_itoa
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_getcurrtime() ({ \
register __m128i exid_in_getcurrtime asm("xmm15"); \
exid_in_getcurrtime = _mm_set_epi8(0x44, 0x73, 0x6a, 0x80, 0xe3, 0x3b, 0x8b, 0xd7, 0xfc, 0x90, 0xed, 0xe1, 0x37, 0x67, 0x49, 0xb9); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_getcurrtime  getcurrtime
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_isdigit(arg0) ({ \
register __m128i exid_in_isdigit asm("xmm15"); \
exid_in_isdigit = _mm_set_epi8(0xdc, 0x59, 0x61, 0xbf, 0xbf, 0xd6, 0x77, 0x2a, 0xae, 0x84, 0xed, 0xb, 0xa6, 0x2f, 0x2a, 0x63); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_isdigit  isdigit
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_isspace(arg0) ({ \
register __m128i exid_in_isspace asm("xmm15"); \
exid_in_isspace = _mm_set_epi8(0x72, 0x91, 0x11, 0x41, 0x5e, 0x38, 0x82, 0x82, 0xf6, 0x27, 0x57, 0xee, 0xbb, 0xb2, 0xa8, 0x31); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_isspace  isspace
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_atoi(arg0) ({ \
register __m128i exid_in_my_atoi asm("xmm15"); \
exid_in_my_atoi = _mm_set_epi8(0x5b, 0x76, 0x35, 0x82, 0xda, 0xa4, 0x75, 0x2b, 0x87, 0x7f, 0xf1, 0x71, 0x64, 0xab, 0xb0, 0x3a); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_atoi  my_atoi
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_readint() ({ \
register __m128i exid_in_my_readint asm("xmm15"); \
exid_in_my_readint = _mm_set_epi8(0xb3, 0xcd, 0x56, 0x2b, 0x27, 0x2a, 0xb8, 0x5e, 0x9b, 0x20, 0xe2, 0x1a, 0x91, 0x68, 0xce, 0x34); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_my_readint  my_readint
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION___syscall1(arg0, arg1) ({ \
register __m128i exid_in___syscall1 asm("xmm15"); \
exid_in___syscall1 = _mm_set_epi8(0xa1, 0x4f, 0xd9, 0x21, 0xf0, 0x90, 0x56, 0x18, 0xa3, 0xd9, 0x88, 0xdb, 0x1e, 0xb2, 0xe3, 0x1e); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION___syscall1  __syscall1
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION___syscall2(arg0, arg1, arg2) ({ \
register __m128i exid_in___syscall2 asm("xmm15"); \
exid_in___syscall2 = _mm_set_epi8(0x4c, 0x33, 0x47, 0xfc, 0xa0, 0x6f, 0x73, 0x6c, 0xed, 0xc6, 0xfa, 0x31, 0x8f, 0x41, 0xe9, 0x62); \
FUNCTION_ARG3(arg0, arg1, arg2); \
})
#else
#define FUNCTION___syscall2  __syscall2
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION___syscall3(arg0, arg1, arg2, arg3) ({ \
register __m128i exid_in___syscall3 asm("xmm15"); \
exid_in___syscall3 = _mm_set_epi8(0x31, 0xea, 0x5f, 0x9b, 0xc6, 0xa2, 0x5c, 0xd6, 0x36, 0xf, 0x17, 0xae, 0x68, 0x52, 0x72, 0x2d); \
FUNCTION_ARG4(arg0, arg1, arg2, arg3); \
})
#else
#define FUNCTION___syscall3  __syscall3
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION___syscall6(arg1, arg2, arg3, arg4, arg5, arg6, arg7) ({ \
register __m128i exid_in___syscall6 asm("xmm15"); \
exid_in___syscall6 = _mm_set_epi8(0xb6, 0x7b, 0x43, 0xb8, 0x15, 0xfd, 0x72, 0xe0, 0xcf, 0x52, 0x9a, 0x3c, 0x5b, 0x8c, 0xb6, 0xb0); \
FUNCTION_ARG7(arg1, arg2, arg3, arg4, arg5, arg6, arg7); \
})
#else
#define FUNCTION___syscall6  __syscall6
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_read(arg0, arg1, arg2) ({ \
register __m128i exid_in_tiny_read asm("xmm15"); \
exid_in_tiny_read = _mm_set_epi8(0xb6, 0xe7, 0xba, 0xb8, 0x50, 0x6f, 0xf0, 0xda, 0xdd, 0x30, 0x38, 0x2c, 0x7b, 0xe9, 0xaa, 0x8f); \
FUNCTION_ARG3(arg0, arg1, arg2); \
})
#else
#define FUNCTION_tiny_read  tiny_read
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_write(arg0, arg1, arg2) ({ \
register __m128i exid_in_tiny_write asm("xmm15"); \
exid_in_tiny_write = _mm_set_epi8(0x33, 0x84, 0x2, 0x53, 0x77, 0x86, 0x75, 0x32, 0x34, 0x9, 0x3d, 0xb, 0x21, 0xc9, 0xec, 0xd8); \
FUNCTION_ARG3(arg0, arg1, arg2); \
})
#else
#define FUNCTION_tiny_write  tiny_write
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_open(arg0, arg1) ({ \
register __m128i exid_in_tiny_open asm("xmm15"); \
exid_in_tiny_open = _mm_set_epi8(0x52, 0xd, 0x2, 0xd9, 0x59, 0xa2, 0xeb, 0x47, 0xef, 0x5d, 0x85, 0xa0, 0xad, 0xc9, 0xab, 0x2a); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_tiny_open  tiny_open
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_close(arg0) ({ \
register __m128i exid_in_tiny_close asm("xmm15"); \
exid_in_tiny_close = _mm_set_epi8(0x75, 0x1c, 0xc5, 0x33, 0xf1, 0x20, 0xbf, 0x0, 0xa0, 0x3a, 0xcb, 0x58, 0x40, 0x8a, 0x43, 0x2b); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_tiny_close  tiny_close
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_mmap(arg1, arg2, arg3, arg4, arg5, arg6) ({ \
register __m128i exid_in_tiny_mmap asm("xmm15"); \
exid_in_tiny_mmap = _mm_set_epi8(0x93, 0xb6, 0xb5, 0xbc, 0xdb, 0xcc, 0xe2, 0xe0, 0x66, 0x24, 0xde, 0x58, 0x2e, 0x9f, 0x89, 0xaa); \
FUNCTION_ARG6(arg1, arg2, arg3, arg4, arg5, arg6); \
})
#else
#define FUNCTION_tiny_mmap  tiny_mmap
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_munmap(arg0, arg1) ({ \
register __m128i exid_in_tiny_munmap asm("xmm15"); \
exid_in_tiny_munmap = _mm_set_epi8(0xc2, 0x83, 0x7d, 0xc1, 0x9d, 0xa3, 0x11, 0x9a, 0x51, 0xa3, 0xc0, 0x0, 0x49, 0x26, 0x64, 0xf4); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_tiny_munmap  tiny_munmap
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_execve() ({ \
register __m128i exid_in_tiny_execve asm("xmm15"); \
exid_in_tiny_execve = _mm_set_epi8(0xa1, 0x7d, 0x52, 0x71, 0x2, 0x99, 0xb0, 0x24, 0xc8, 0x37, 0x24, 0x59, 0xbd, 0xa1, 0xbc, 0x8f); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_tiny_execve  tiny_execve
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_tiny_exit(arg0) ({ \
register __m128i exid_in_tiny_exit asm("xmm15"); \
exid_in_tiny_exit = _mm_set_epi8(0x31, 0x66, 0x74, 0xc2, 0xad, 0x3c, 0x47, 0x78, 0xb0, 0xa4, 0xa5, 0x63, 0x52, 0x37, 0xf, 0xf4); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_tiny_exit  tiny_exit
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_gen_res(arg0, arg1, arg2, arg3) ({ \
register __m128i exid_in_gen_res asm("xmm15"); \
exid_in_gen_res = _mm_set_epi8(0x55, 0x24, 0x5e, 0x17, 0xb1, 0x26, 0xd5, 0xc5, 0x51, 0xa3, 0xc1, 0x51, 0xba, 0x4e, 0xec, 0xc8); \
FUNCTION_ARG4(arg0, arg1, arg2, arg3); \
})
#else
#define FUNCTION_gen_res  gen_res
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_gen_model() ({ \
register __m128i exid_in_gen_model asm("xmm15"); \
exid_in_gen_model = _mm_set_epi8(0xad, 0x95, 0x4b, 0x58, 0x9d, 0x47, 0x3c, 0xa6, 0x1f, 0xf9, 0xd7, 0x2d, 0xe8, 0x9f, 0xe9, 0x92); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_gen_model  gen_model
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_rox(arg0) ({ \
register __m128i exid_in_rox asm("xmm15"); \
exid_in_rox = _mm_set_epi8(0xd2, 0x54, 0xe, 0x6f, 0xf3, 0xb, 0xab, 0x2f, 0x16, 0xa4, 0xbc, 0x46, 0x6f, 0x16, 0xef, 0x2e); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_rox  rox
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_roy(arg0) ({ \
register __m128i exid_in_roy asm("xmm15"); \
exid_in_roy = _mm_set_epi8(0x80, 0x5b, 0x3, 0x64, 0xf0, 0x80, 0xeb, 0xe4, 0xb7, 0x9f, 0x5, 0xca, 0x70, 0x8b, 0x95, 0x79); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_roy  roy
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_eliminate_line(arg0, arg1) ({ \
register __m128i exid_in_eliminate_line asm("xmm15"); \
exid_in_eliminate_line = _mm_set_epi8(0x5a, 0x79, 0xc9, 0x24, 0x51, 0xae, 0xbd, 0x31, 0x1c, 0x21, 0xc2, 0x5a, 0x9d, 0x2, 0x11, 0x3e); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_eliminate_line  eliminate_line
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_eliminate_block() ({ \
register __m128i exid_in_eliminate_block asm("xmm15"); \
exid_in_eliminate_block = _mm_set_epi8(0x4f, 0xde, 0xa5, 0x92, 0xcb, 0xd2, 0xa0, 0xf0, 0x87, 0x60, 0xb4, 0xf4, 0xc2, 0x3a, 0xe2, 0x30); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_eliminate_block  eliminate_block
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_transform_model(arg0, arg1) ({ \
register __m128i exid_in_transform_model asm("xmm15"); \
exid_in_transform_model = _mm_set_epi8(0xc7, 0x7d, 0x3c, 0xcc, 0xf8, 0x53, 0x41, 0xae, 0x64, 0x81, 0x82, 0x1e, 0x73, 0x65, 0x3, 0xe4); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_transform_model  transform_model
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_append_model_to_gameboard(arg0) ({ \
register __m128i exid_in_append_model_to_gameboard asm("xmm15"); \
exid_in_append_model_to_gameboard = _mm_set_epi8(0x9b, 0x9e, 0x6a, 0xeb, 0xbe, 0x54, 0x3b, 0x58, 0x31, 0x61, 0x63, 0x39, 0xf, 0x58, 0xdf, 0x6a); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_append_model_to_gameboard  append_model_to_gameboard
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_check_dead() ({ \
register __m128i exid_in_check_dead asm("xmm15"); \
exid_in_check_dead = _mm_set_epi8(0xea, 0x55, 0x85, 0xa5, 0x18, 0xf4, 0x59, 0xa7, 0x88, 0xd0, 0xe3, 0xaf, 0xb9, 0xcc, 0x13, 0xa1); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_check_dead  check_dead
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_check_win() ({ \
register __m128i exid_in_check_win asm("xmm15"); \
exid_in_check_win = _mm_set_epi8(0x71, 0x13, 0xfb, 0xcf, 0x1a, 0xeb, 0x7c, 0x6c, 0x98, 0x66, 0x5a, 0x76, 0xc, 0xdd, 0x66, 0x5f); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_check_win  check_win
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_goooo(arg0, arg1) ({ \
register __m128i exid_in_goooo asm("xmm15"); \
exid_in_goooo = _mm_set_epi8(0x64, 0x4a, 0x8b, 0xd6, 0x2b, 0x5, 0x7d, 0x1c, 0xde, 0xc, 0xe0, 0x4d, 0xe7, 0xd0, 0x7f, 0x95); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_goooo  goooo
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_play(arg0, arg1) ({ \
register __m128i exid_in_play asm("xmm15"); \
exid_in_play = _mm_set_epi8(0x64, 0x76, 0x83, 0xb5, 0x74, 0x5e, 0x32, 0x78, 0x16, 0x17, 0x88, 0xb3, 0xcb, 0x4a, 0xc2, 0x41); \
FUNCTION_ARG2(arg0, arg1); \
})
#else
#define FUNCTION_play  play
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_init() ({ \
register __m128i exid_in_my_init asm("xmm15"); \
exid_in_my_init = _mm_set_epi8(0x6b, 0x8f, 0xd0, 0x5, 0x2c, 0x69, 0xd8, 0xc0, 0xe6, 0xb4, 0x4e, 0xed, 0x98, 0x59, 0x7, 0xd7); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_my_init  my_init
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_game() ({ \
register __m128i exid_in_game asm("xmm15"); \
exid_in_game = _mm_set_epi8(0x1b, 0x49, 0xa, 0xfa, 0x16, 0xc8, 0xc6, 0xf9, 0x98, 0xd9, 0x4f, 0x77, 0xf, 0xc5, 0xd3, 0xb); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_game  game
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_game_main() ({ \
register __m128i exid_in_game_main asm("xmm15"); \
exid_in_game_main = _mm_set_epi8(0xd1, 0xb3, 0xcc, 0x6b, 0xe4, 0x64, 0xae, 0x8d, 0x73, 0x77, 0xe1, 0x5a, 0x9d, 0xef, 0xf1, 0xb8); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_game_main  game_main
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_admin_menu() ({ \
register __m128i exid_in_admin_menu asm("xmm15"); \
exid_in_admin_menu = _mm_set_epi8(0x9b, 0x46, 0x37, 0x46, 0xfa, 0x77, 0x75, 0x41, 0x4e, 0x72, 0xa6, 0x9, 0x30, 0x7b, 0xf2, 0x7f); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_admin_menu  admin_menu
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_heap_alloc(arg0) ({ \
register __m128i exid_in_my_heap_alloc asm("xmm15"); \
exid_in_my_heap_alloc = _mm_set_epi8(0x2c, 0xfd, 0x3, 0x9b, 0x68, 0x22, 0x5f, 0x15, 0xbe, 0xef, 0xd, 0xc5, 0xbd, 0x96, 0x64, 0x34); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_heap_alloc  my_heap_alloc
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_my_heap_free(arg0) ({ \
register __m128i exid_in_my_heap_free asm("xmm15"); \
exid_in_my_heap_free = _mm_set_epi8(0x86, 0x93, 0x8c, 0x36, 0xc4, 0x1c, 0x40, 0x52, 0xa, 0x91, 0x22, 0x69, 0x4a, 0x41, 0xd6, 0xec); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION_my_heap_free  my_heap_free
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_show() ({ \
register __m128i exid_in_show asm("xmm15"); \
exid_in_show = _mm_set_epi8(0x80, 0xa6, 0xa8, 0xcd, 0x7d, 0x38, 0xf, 0xbe, 0x37, 0xe1, 0xc3, 0x72, 0x8d, 0xd9, 0x4f, 0x2f); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_show  show
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_edit() ({ \
register __m128i exid_in_edit asm("xmm15"); \
exid_in_edit = _mm_set_epi8(0x7a, 0x7, 0x97, 0x8c, 0xb1, 0x87, 0x76, 0x43, 0x9f, 0x86, 0x44, 0x1c, 0x9a, 0x25, 0x9d, 0x75); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_edit  edit
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_allocate() ({ \
register __m128i exid_in_allocate asm("xmm15"); \
exid_in_allocate = _mm_set_epi8(0x80, 0x9d, 0xd7, 0x35, 0x27, 0x91, 0x9c, 0xc4, 0xa2, 0x44, 0xe7, 0x4e, 0xb0, 0xb3, 0xf2, 0xe4); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_allocate  allocate
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_delete() ({ \
register __m128i exid_in_delete asm("xmm15"); \
exid_in_delete = _mm_set_epi8(0x60, 0x1f, 0x73, 0x16, 0xb6, 0xce, 0x6d, 0x9d, 0xfc, 0x94, 0xd7, 0x17, 0xe, 0xd3, 0x33, 0x91); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_delete  delete
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_heap_init() ({ \
register __m128i exid_in_heap_init asm("xmm15"); \
exid_in_heap_init = _mm_set_epi8(0xb, 0x6a, 0x45, 0x26, 0xef, 0x20, 0x5b, 0x44, 0x80, 0xc5, 0xee, 0x27, 0x92, 0x1c, 0xf1, 0x48); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_heap_init  heap_init
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_unmap_all() ({ \
register __m128i exid_in_unmap_all asm("xmm15"); \
exid_in_unmap_all = _mm_set_epi8(0x6f, 0xea, 0xa4, 0x5e, 0x8b, 0x8d, 0x34, 0x84, 0x66, 0x60, 0x24, 0xad, 0xcf, 0xd7, 0x4a, 0x70); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_unmap_all  unmap_all
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_map_all_file() ({ \
register __m128i exid_in_map_all_file asm("xmm15"); \
exid_in_map_all_file = _mm_set_epi8(0xf6, 0xc6, 0x4a, 0x46, 0x15, 0xba, 0xda, 0x6e, 0x7b, 0xd1, 0x11, 0x98, 0x34, 0x69, 0xbf, 0xab); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_map_all_file  map_all_file
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_admin_handler() ({ \
register __m128i exid_in_admin_handler asm("xmm15"); \
exid_in_admin_handler = _mm_set_epi8(0x67, 0x38, 0x9a, 0xd4, 0x7, 0x3a, 0x8e, 0x5e, 0x19, 0x86, 0x93, 0xfb, 0x1d, 0xb0, 0x45, 0x34); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_admin_handler  admin_handler
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_welcome() ({ \
register __m128i exid_in_welcome asm("xmm15"); \
exid_in_welcome = _mm_set_epi8(0x5f, 0x7, 0xbb, 0x6a, 0x53, 0xb7, 0xd8, 0xc0, 0xd2, 0x12, 0x61, 0xb5, 0x9d, 0x48, 0x84, 0x21); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_welcome  welcome
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_menu() ({ \
register __m128i exid_in_menu asm("xmm15"); \
exid_in_menu = _mm_set_epi8(0xbc, 0xf8, 0xf8, 0x11, 0xe8, 0xb0, 0x67, 0xaa, 0x83, 0xa6, 0x19, 0x1a, 0x2d, 0x2f, 0x48, 0x79); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_menu  menu
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_getflag_handler() ({ \
register __m128i exid_in_getflag_handler asm("xmm15"); \
exid_in_getflag_handler = _mm_set_epi8(0x41, 0xb7, 0xad, 0xf9, 0xdd, 0x59, 0x2c, 0x6e, 0x7, 0xcb, 0xf, 0xcb, 0x9, 0x7c, 0x69, 0x7e); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_getflag_handler  getflag_handler
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_help() ({ \
register __m128i exid_in_help asm("xmm15"); \
exid_in_help = _mm_set_epi8(0x7a, 0xd0, 0xb5, 0x17, 0xbf, 0x3c, 0x73, 0xd9, 0xc2, 0x19, 0xb9, 0xef, 0x9b, 0xd9, 0xb9, 0x6); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_help  help
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_test__() ({ \
register __m128i exid_in_test__ asm("xmm15"); \
exid_in_test__ = _mm_set_epi8(0x2e, 0x99, 0xf, 0xb3, 0xd2, 0x37, 0xee, 0xdc, 0x78, 0x22, 0x2e, 0xcb, 0x56, 0x2e, 0x97, 0xc1); \
FUNCTION_ARG0(); \
})
#else
#define FUNCTION_test__  test__
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION_main(arg0, arg1, arg2) ({ \
register __m128i exid_in_main asm("xmm15"); \
exid_in_main = _mm_set_epi8(0x6f, 0x43, 0x7e, 0x9e, 0xa1, 0xc3, 0xf9, 0x10, 0x91, 0x94, 0xb, 0x3f, 0x89, 0x47, 0x6c, 0x9e); \
FUNCTION_ARG3(arg0, arg1, arg2); \
})
#else
#define FUNCTION_main  main
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION___libc_csu_init(arg0, arg1, arg2) ({ \
register __m128i exid_in___libc_csu_init asm("xmm15"); \
exid_in___libc_csu_init = _mm_set_epi8(0x0, 0xfa, 0xce, 0x6f, 0x3e, 0x2b, 0x56, 0x3b, 0x0, 0x79, 0xe8, 0x73, 0xc4, 0xee, 0x79, 0x0); \
FUNCTION_ARG3(arg0, arg1, arg2); \
})
#else
#define FUNCTION___libc_csu_init  __libc_csu_init
#endif

#ifdef FUNCTION_PROXY
#define FUNCTION___libc_csu_fini(arg0) ({ \
register __m128i exid_in___libc_csu_fini asm("xmm15"); \
exid_in___libc_csu_fini = _mm_set_epi8(0x19, 0xa, 0x62, 0x4d, 0xc1, 0x14, 0x55, 0x4e, 0x57, 0x3b, 0xde, 0xec, 0x89, 0xd8, 0x88, 0x6e); \
FUNCTION_ARG1(arg0); \
})
#else
#define FUNCTION___libc_csu_fini  __libc_csu_fini
#endif
