#define BSS_PROXY

#define BSS_BASE 0x700000000


#define BSS_PROXY_completed_7698 0x0
#define BSS_PROXY_game_score 0x8
#define BSS_PROXY_is_admin 0x10
#define BSS_PROXY_ptr_size 0x20
#define BSS_PROXY_heap_bins 0x60
#define BSS_PROXY_gv_heap 0xc0
#define BSS_PROXY_ptr 0x128
#define BSS_PROXY_rand_seed 0x120
#define BSS_PROXY_gameboard 0x1a8
#define BSS_PROXY_sc_addr 0x1b8





#ifdef BSS_PROXY
#define S_completed_7698 (BSS_BASE+BSS_PROXY_completed_7698)
#else
#define S_completed_7698 completed_7698
#endif


#ifdef BSS_PROXY
#define S_game_score (*(uint64_t *)(BSS_BASE+BSS_PROXY_game_score))
#else
#define S_game_score game_score
#endif


#ifdef BSS_PROXY
#define S_is_admin (*(int *)(BSS_BASE+BSS_PROXY_is_admin))
#else
#define S_is_admin is_admin
#endif


#ifdef BSS_PROXY
#define S_ptr_size ((int *)(BSS_BASE+BSS_PROXY_ptr_size))
#else
#define S_ptr_size ptr_size
#endif


#ifdef BSS_PROXY
#define S_heap_bins ((bin_t *)(BSS_BASE+BSS_PROXY_heap_bins))
#else
#define S_heap_bins heap_bins
#endif


#ifdef BSS_PROXY
#define S_gv_heap (*(heap_t *)(BSS_BASE+BSS_PROXY_gv_heap))
#else
#define S_gv_heap gv_heap
#endif


#ifdef BSS_PROXY
#define S_ptr ((char **)(BSS_BASE+BSS_PROXY_ptr))
#else
#define S_ptr ptr
#endif


#ifdef BSS_PROXY
#define S_rand_seed (*(uint64_t *)(BSS_BASE+BSS_PROXY_rand_seed))
#else
#define S_rand_seed rand_seed
#endif


#ifdef BSS_PROXY
#define S_gameboard ((gamboard_type *)(BSS_BASE+BSS_PROXY_gameboard))
#else
#define S_gameboard gameboard
#endif


#ifdef BSS_PROXY
#define S_sc_addr ((func_block_st__ **)(BSS_BASE+BSS_PROXY_sc_addr))
#else
#define S_sc_addr sc_addr
#endif

