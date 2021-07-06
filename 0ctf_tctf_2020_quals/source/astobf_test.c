//
// Created by G6 on 2020-06-21.
//

// gcc -m32 -O2 -s astobf_test.c -o astobf

#include <stdarg.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "astobf.h"
#include "astobf_test.h"

//void *extern_func[100];

// flag{HEY!Lumpy!!W@tcH_0ut_My_TrEe!!}

__attribute__((constructor))
void init_DeclRef() {

//    DeclRef[0] = (void *) memset;
//    DeclRef[1] = (void *) scanf;
//    DeclRef[2] = (void *) puts;
//    DeclRef[3] = (void *) NULL;
//    DeclRef[4] = (void *) & "Ah?";
//    DeclRef[5] = (void *) & "%36s";
//    DeclRef[6] = (void *) & "Wow!";
//    DeclRef[7] = (void *) & "Ow!";
    DeclRef[2] = (void *) puts;
    DeclRef[7] = (void *) NULL;
    DeclRef[6] = (void *) NULL;
    DeclRef[1] = (void *) scanf;
    DeclRef[0] = (void *) memset;
    DeclRef[9] = (void *) &"Ow!";
    DeclRef[5] = (void *) &"%36s";
    DeclRef[8] = (void *) &"Wow!";
    DeclRef[3] = (void *) NULL;
    DeclRef[4] = (void *) &"Ah?";
}


int main() {
//    init_DeclRef();
//    init_node();

    node0.func(&node0, 0);

    return 0;
}

