验证的算法：astobf_chall.c
Dump出验证算法的AST
clang -Xclang -ast-dump ./astobf_chall.c > out.txt

处理该ast：python2 ./6-21-astobf.py
其中进行node的生成和初始化，将print出的c初始化代码copy至astobf_test.h
（若修改astobf_chall.c，需要对py中的一些变量进行修改）

astobf_test.c astobf_test.h包含node的结构及handler
gcc -m32 -O2 -g astobf_test.c -o astobf_debug
gcc -m32 -O2 -s astobf_test.c -o astobf