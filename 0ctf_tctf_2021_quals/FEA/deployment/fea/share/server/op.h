#define NUM_BITS 8
#define MASK 0xFFFFFFFF

__inline__ __attribute__((always_inline))
uint32_t add(uint32_t a, uint32_t b) {
    return a+b;
}
__inline__ __attribute__((always_inline))
uint32_t sub(uint32_t a, uint32_t b) {
    return a-b;
}
__inline__ __attribute__((always_inline))
uint32_t mul(uint32_t a, uint32_t b) {
    return a*b;
}
__inline__ __attribute__((always_inline))
uint32_t div(uint32_t a, uint32_t b) {
    return a/b;
}
__inline__ __attribute__((always_inline))
uint32_t mod(uint32_t a, uint32_t b) {
    return a%b;
}
__inline__ __attribute__((always_inline))
uint32_t ror(uint32_t a, uint32_t b) {
    return (a >> (b%NUM_BITS)) | ((a << (NUM_BITS - (b%NUM_BITS))) & MASK);
}
__inline__ __attribute__((always_inline))
uint32_t rol(uint32_t a, uint32_t b) {
    return ((a << (b%NUM_BITS)) & MASK) | (a >> (NUM_BITS - (b%NUM_BITS)));
}
__inline__ __attribute__((always_inline))
uint32_t bit_xor(uint32_t a, uint32_t b) {
    return a^b;
}
__inline__ __attribute__((always_inline))
uint32_t bit_and(uint32_t a, uint32_t b) {
    return a&b;
}
__inline__ __attribute__((always_inline))
uint32_t bit_or(uint32_t a, uint32_t b) {
    return a|b;
}
