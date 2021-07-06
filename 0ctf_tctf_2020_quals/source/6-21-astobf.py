import random
import re


# clang -Xclang -ast-dump astobf_chall.c > out.txt

ast = """`-FunctionDecl  line:99:6 main 'void ()'
  `-CompoundStmt 
    |-DeclStmt 
    | `-VarDecl  col:14 used input_str 'uint32_t [20]'
    |-CallExpr  'void *'
    | |-ImplicitCastExpr  'void *(*)(void *, int, unsigned long)' <FunctionToPointerDecay>
    | | `-DeclRefExpr  'void *(void *, int, unsigned long)' Function 0x55f4f654ef70 'memset' 'void *(void *, int, unsigned long)'
    | |-ImplicitCastExpr  'void *' <BitCast>
    | | `-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
    | |   `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
    | |-IntegerLiteral  'int' 0
    | `-ImplicitCastExpr  'unsigned long' <IntegralCast>
    |   `-IntegerLiteral  'int' 80
    |-CallExpr  'int'
    | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
    | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
    | `-ImplicitCastExpr  'const char *' <NoOp>
    |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
    |     `-StringLiteral  'char [4]' lvalue "Ah?"
    |-CallExpr  'int'
    | |-ImplicitCastExpr  'int (*)(const char *restrict, ...)' <FunctionToPointerDecay>
    | | `-DeclRefExpr  'int (const char *restrict, ...)' Function 0x55f4f657fea8 'scanf' 'int (const char *restrict, ...)'
    | |-ImplicitCastExpr  'const char *' <NoOp>
    | | `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
    | |   `-StringLiteral  'char [5]' lvalue "%36s"
    | `-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
    |   `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
    `-IfStmt  has_else
      |-BinaryOperator  'int' '=='
      | |-ParenExpr  'unsigned int'
      | | `-BinaryOperator  'unsigned int' '^'
      | |   |-ParenExpr  'unsigned int'
      | |   | `-BinaryOperator  'unsigned int' '^'
      | |   |   |-ParenExpr  'unsigned int'
      | |   |   | `-BinaryOperator  'unsigned int' '^'
      | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |   |   |   |   `-IntegerLiteral  'int' 0
      | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |   |   |       |   `-IntegerLiteral  'int' 0
      | |   |   |       `-IntegerLiteral  'int' 13
      | |   |   `-ParenExpr  'unsigned int'
      | |   |     `-BinaryOperator  'unsigned int' '>>'
      | |   |       |-ParenExpr  'unsigned int'
      | |   |       | `-BinaryOperator  'unsigned int' '^'
      | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |   |       |   |   `-IntegerLiteral  'int' 0
      | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |   |       |       |   `-IntegerLiteral  'int' 0
      | |   |       |       `-IntegerLiteral  'int' 13
      | |   |       `-IntegerLiteral  'int' 17
      | |   `-ParenExpr  'unsigned int'
      | |     `-BinaryOperator  'unsigned int' '<<'
      | |       |-ParenExpr  'unsigned int'
      | |       | `-BinaryOperator  'unsigned int' '^'
      | |       |   |-ParenExpr  'unsigned int'
      | |       |   | `-BinaryOperator  'unsigned int' '^'
      | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |       |   |   |   `-IntegerLiteral  'int' 0
      | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |       |   |       |   `-IntegerLiteral  'int' 0
      | |       |   |       `-IntegerLiteral  'int' 13
      | |       |   `-ParenExpr  'unsigned int'
      | |       |     `-BinaryOperator  'unsigned int' '>>'
      | |       |       |-ParenExpr  'unsigned int'
      | |       |       | `-BinaryOperator  'unsigned int' '^'
      | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |       |       |   |   `-IntegerLiteral  'int' 0
      | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      | |       |       |       |   `-IntegerLiteral  'int' 0
      | |       |       |       `-IntegerLiteral  'int' 13
      | |       |       `-IntegerLiteral  'int' 17
      | |       `-IntegerLiteral  'int' 5
      | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   `-BinaryOperator  'int' '*'
      |     |-BinaryOperator  'int' '*'
      |     | |-BinaryOperator  'int' '*'
      |     | | |-BinaryOperator  'int' '*'
      |     | | | |-ParenExpr  'int'
      |     | | | | `-BinaryOperator  'int' '+'
      |     | | | |   |-BinaryOperator  'int' '*'
      |     | | | |   | |-BinaryOperator  'int' '*'
      |     | | | |   | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |-ParenExpr  'int'
      |     | | | |   | | | | | `-BinaryOperator  'int' '+'
      |     | | | |   | | | | |   |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |-ParenExpr  'int'
      |     | | | |   | | | | |   | | | | | `-BinaryOperator  'int' '+'
      |     | | | |   | | | | |   | | | | |   |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | | | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | | | | | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | | | | | | |-ParenExpr  'int'
      |     | | | |   | | | | |   | | | | |   | | | | | | | | `-BinaryOperator  'int' '+'
      |     | | | |   | | | | |   | | | | |   | | | | | | | |   |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | | | | | | |   | |-BinaryOperator  'int' '*'
      |     | | | |   | | | | |   | | | | |   | | | | | | | |   | | |-IntegerLiteral  'int' 1
      |     | | | |   | | | | |   | | | | |   | | | | | | | |   | | `-IntegerLiteral  'int' 2
      |     | | | |   | | | | |   | | | | |   | | | | | | | |   | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | | | |   | | | | | | | |   `-IntegerLiteral  'int' 1
      |     | | | |   | | | | |   | | | | |   | | | | | | | `-IntegerLiteral  'int' 2
      |     | | | |   | | | | |   | | | | |   | | | | | | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | | | |   | | | | | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | | | |   | | | | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | | | |   | | | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | | | |   | | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | | | |   | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | | | |   `-IntegerLiteral  'int' 1
      |     | | | |   | | | | |   | | | | `-IntegerLiteral  'int' 2
      |     | | | |   | | | | |   | | | `-IntegerLiteral  'int' 3
      |     | | | |   | | | | |   | | `-IntegerLiteral  'int' 5
      |     | | | |   | | | | |   | `-IntegerLiteral  'int' 5
      |     | | | |   | | | | |   `-IntegerLiteral  'int' 1
      |     | | | |   | | | | `-IntegerLiteral  'int' 2
      |     | | | |   | | | `-IntegerLiteral  'int' 2
      |     | | | |   | | `-IntegerLiteral  'int' 2
      |     | | | |   | `-IntegerLiteral  'int' 2
      |     | | | |   `-IntegerLiteral  'int' 1
      |     | | | `-IntegerLiteral  'int' 2
      |     | | `-IntegerLiteral  'int' 2
      |     | `-IntegerLiteral  'int' 2
      |     `-IntegerLiteral  'int' 2
      |-CompoundStmt 
      | `-IfStmt  has_else
      |   |-BinaryOperator  'int' '=='
      |   | |-ParenExpr  'unsigned int'
      |   | | `-BinaryOperator  'unsigned int' '^'
      |   | |   |-ParenExpr  'unsigned int'
      |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   | |   |   |-ParenExpr  'unsigned int'
      |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |   |   |   |   `-IntegerLiteral  'int' 1
      |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |   |   |       |   `-IntegerLiteral  'int' 1
      |   | |   |   |       `-IntegerLiteral  'int' 13
      |   | |   |   `-ParenExpr  'unsigned int'
      |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   | |   |       |-ParenExpr  'unsigned int'
      |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |   |       |   |   `-IntegerLiteral  'int' 1
      |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |   |       |       |   `-IntegerLiteral  'int' 1
      |   | |   |       |       `-IntegerLiteral  'int' 13
      |   | |   |       `-IntegerLiteral  'int' 17
      |   | |   `-ParenExpr  'unsigned int'
      |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   | |       |-ParenExpr  'unsigned int'
      |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   | |       |   |-ParenExpr  'unsigned int'
      |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |       |   |   |   `-IntegerLiteral  'int' 1
      |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |       |   |       |   `-IntegerLiteral  'int' 1
      |   | |       |   |       `-IntegerLiteral  'int' 13
      |   | |       |   `-ParenExpr  'unsigned int'
      |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   | |       |       |-ParenExpr  'unsigned int'
      |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |       |       |   |   `-IntegerLiteral  'int' 1
      |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   | |       |       |       |   `-IntegerLiteral  'int' 1
      |   | |       |       |       `-IntegerLiteral  'int' 13
      |   | |       |       `-IntegerLiteral  'int' 17
      |   | |       `-IntegerLiteral  'int' 5
      |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   `-BinaryOperator  'int' '*'
      |   |     |-BinaryOperator  'int' '*'
      |   |     | |-ParenExpr  'int'
      |   |     | | `-BinaryOperator  'int' '+'
      |   |     | |   |-BinaryOperator  'int' '*'
      |   |     | |   | |-BinaryOperator  'int' '*'
      |   |     | |   | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |-ParenExpr  'int'
      |   |     | |   | | | | `-BinaryOperator  'int' '+'
      |   |     | |   | | | |   |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |-ParenExpr  'int'
      |   |     | |   | | | |   | | | | `-BinaryOperator  'int' '+'
      |   |     | |   | | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |-ParenExpr  'int'
      |   |     | |   | | | |   | | | |   | | | | `-BinaryOperator  'int' '+'
      |   |     | |   | | | |   | | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |-ParenExpr  'int'
      |   |     | |   | | | |   | | | |   | | | |   | | | | | `-BinaryOperator  'int' '+'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |-ParenExpr  'int'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | | `-BinaryOperator  'int' '+'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | | | |-BinaryOperator  'int' '*'
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | | | | |-IntegerLiteral  'int' 1
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   | `-IntegerLiteral  'int' 5
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   | `-IntegerLiteral  'int' 3
      |   |     | |   | | | |   | | | |   | | | |   | | | | |   `-IntegerLiteral  'int' 1
      |   |     | |   | | | |   | | | |   | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | | |   | `-IntegerLiteral  'int' 5
      |   |     | |   | | | |   | | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |     | |   | | | |   | | | |   | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | | |   | | `-IntegerLiteral  'int' 5
      |   |     | |   | | | |   | | | |   | `-IntegerLiteral  'int' 5
      |   |     | |   | | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |     | |   | | | |   | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | | |   | | `-IntegerLiteral  'int' 3
      |   |     | |   | | | |   | `-IntegerLiteral  'int' 5
      |   |     | |   | | | |   `-IntegerLiteral  'int' 1
      |   |     | |   | | | `-IntegerLiteral  'int' 2
      |   |     | |   | | `-IntegerLiteral  'int' 2
      |   |     | |   | `-IntegerLiteral  'int' 3
      |   |     | |   `-IntegerLiteral  'int' 1
      |   |     | `-IntegerLiteral  'int' 2
      |   |     `-IntegerLiteral  'int' 3
      |   |-CompoundStmt 
      |   | `-IfStmt  has_else
      |   |   |-BinaryOperator  'int' '=='
      |   |   | |-ParenExpr  'unsigned int'
      |   |   | | `-BinaryOperator  'unsigned int' '^'
      |   |   | |   |-ParenExpr  'unsigned int'
      |   |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   |   | |   |   |-ParenExpr  'unsigned int'
      |   |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |   |   |   |   `-IntegerLiteral  'int' 2
      |   |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |   |   |       |   `-IntegerLiteral  'int' 2
      |   |   | |   |   |       `-IntegerLiteral  'int' 13
      |   |   | |   |   `-ParenExpr  'unsigned int'
      |   |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   |   | |   |       |-ParenExpr  'unsigned int'
      |   |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |   |       |   |   `-IntegerLiteral  'int' 2
      |   |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |   |       |       |   `-IntegerLiteral  'int' 2
      |   |   | |   |       |       `-IntegerLiteral  'int' 13
      |   |   | |   |       `-IntegerLiteral  'int' 17
      |   |   | |   `-ParenExpr  'unsigned int'
      |   |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   |   | |       |-ParenExpr  'unsigned int'
      |   |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   |   | |       |   |-ParenExpr  'unsigned int'
      |   |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |       |   |   |   `-IntegerLiteral  'int' 2
      |   |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |       |   |       |   `-IntegerLiteral  'int' 2
      |   |   | |       |   |       `-IntegerLiteral  'int' 13
      |   |   | |       |   `-ParenExpr  'unsigned int'
      |   |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   |   | |       |       |-ParenExpr  'unsigned int'
      |   |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |       |       |   |   `-IntegerLiteral  'int' 2
      |   |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   | |       |       |       |   `-IntegerLiteral  'int' 2
      |   |   | |       |       |       `-IntegerLiteral  'int' 13
      |   |   | |       |       `-IntegerLiteral  'int' 17
      |   |   | |       `-IntegerLiteral  'int' 5
      |   |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   |   `-ParenExpr  'int'
      |   |   |     `-BinaryOperator  'int' '+'
      |   |   |       |-BinaryOperator  'int' '*'
      |   |   |       | |-BinaryOperator  'int' '*'
      |   |   |       | | |-BinaryOperator  'int' '*'
      |   |   |       | | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |-ParenExpr  'int'
      |   |   |       | | | | | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |-ParenExpr  'int'
      |   |   |       | | | | | |   | | | | | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |-ParenExpr  'int'
      |   |   |       | | | | | |   | | | | | |   | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   | | | | | |   | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |-ParenExpr  'int'
      |   |   |       | | | | | |   | | | | | |   | |   | | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |-ParenExpr  'int'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |-ParenExpr  'int'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |-ParenExpr  'int'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | |-ParenExpr  'int'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | |   | | |-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   | `-IntegerLiteral  'int' 3
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |       | | | | | |   | | | | | |   | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | |   | |   | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | |   | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   | `-IntegerLiteral  'int' 2
      |   |   |       | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |       | | | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | | `-IntegerLiteral  'int' 2
      |   |   |       | | | `-IntegerLiteral  'int' 2
      |   |   |       | | `-IntegerLiteral  'int' 3
      |   |   |       | `-IntegerLiteral  'int' 5
      |   |   |       `-IntegerLiteral  'int' 1
      |   |   |-CompoundStmt 
      |   |   | `-IfStmt  has_else
      |   |   |   |-BinaryOperator  'int' '=='
      |   |   |   | |-ParenExpr  'unsigned int'
      |   |   |   | | `-BinaryOperator  'unsigned int' '^'
      |   |   |   | |   |-ParenExpr  'unsigned int'
      |   |   |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   | |   |   |-ParenExpr  'unsigned int'
      |   |   |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |   |   |   |   `-IntegerLiteral  'int' 3
      |   |   |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |   |   |       |   `-IntegerLiteral  'int' 3
      |   |   |   | |   |   |       `-IntegerLiteral  'int' 13
      |   |   |   | |   |   `-ParenExpr  'unsigned int'
      |   |   |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   | |   |       |-ParenExpr  'unsigned int'
      |   |   |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |   |       |   |   `-IntegerLiteral  'int' 3
      |   |   |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |   |       |       |   `-IntegerLiteral  'int' 3
      |   |   |   | |   |       |       `-IntegerLiteral  'int' 13
      |   |   |   | |   |       `-IntegerLiteral  'int' 17
      |   |   |   | |   `-ParenExpr  'unsigned int'
      |   |   |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   |   |   | |       |-ParenExpr  'unsigned int'
      |   |   |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   | |       |   |-ParenExpr  'unsigned int'
      |   |   |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |       |   |   |   `-IntegerLiteral  'int' 3
      |   |   |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |       |   |       |   `-IntegerLiteral  'int' 3
      |   |   |   | |       |   |       `-IntegerLiteral  'int' 13
      |   |   |   | |       |   `-ParenExpr  'unsigned int'
      |   |   |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   | |       |       |-ParenExpr  'unsigned int'
      |   |   |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |       |       |   |   `-IntegerLiteral  'int' 3
      |   |   |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   | |       |       |       |   `-IntegerLiteral  'int' 3
      |   |   |   | |       |       |       `-IntegerLiteral  'int' 13
      |   |   |   | |       |       `-IntegerLiteral  'int' 17
      |   |   |   | |       `-IntegerLiteral  'int' 5
      |   |   |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   |   |   `-ParenExpr  'int'
      |   |   |   |     `-BinaryOperator  'int' '+'
      |   |   |   |       |-BinaryOperator  'int' '*'
      |   |   |   |       | |-ParenExpr  'int'
      |   |   |   |       | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |-ParenExpr  'int'
      |   |   |   |       | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | |   | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | |-ParenExpr  'int'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | |   | | |-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   | |   | `-IntegerLiteral  'int' 5
      |   |   |   |       | |   | | |   | | | | | | |   | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | |   | | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |       | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |       | |   | `-IntegerLiteral  'int' 5
      |   |   |   |       | |   `-IntegerLiteral  'int' 1
      |   |   |   |       | `-IntegerLiteral  'int' 2
      |   |   |   |       `-IntegerLiteral  'int' 1
      |   |   |   |-CompoundStmt 
      |   |   |   | `-IfStmt  has_else
      |   |   |   |   |-BinaryOperator  'int' '=='
      |   |   |   |   | |-ParenExpr  'unsigned int'
      |   |   |   |   | | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   | |   |-ParenExpr  'unsigned int'
      |   |   |   |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   | |   |   |-ParenExpr  'unsigned int'
      |   |   |   |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |   |   |   |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |   |   |       |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |   |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   | |   |   `-ParenExpr  'unsigned int'
      |   |   |   |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   | |   |       |-ParenExpr  'unsigned int'
      |   |   |   |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |   |       |   |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |   |       |       |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |   |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   | |   |       `-IntegerLiteral  'int' 17
      |   |   |   |   | |   `-ParenExpr  'unsigned int'
      |   |   |   |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   |   |   |   | |       |-ParenExpr  'unsigned int'
      |   |   |   |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   | |       |   |-ParenExpr  'unsigned int'
      |   |   |   |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |       |   |   |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |       |   |       |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |       |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   | |       |   `-ParenExpr  'unsigned int'
      |   |   |   |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   | |       |       |-ParenExpr  'unsigned int'
      |   |   |   |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |       |       |   |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   | |       |       |       |   `-IntegerLiteral  'int' 4
      |   |   |   |   | |       |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   | |       |       `-IntegerLiteral  'int' 17
      |   |   |   |   | |       `-IntegerLiteral  'int' 5
      |   |   |   |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   |   |   |   `-BinaryOperator  'int' '*'
      |   |   |   |   |     |-BinaryOperator  'int' '*'
      |   |   |   |   |     | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |-ParenExpr  'int'
      |   |   |   |   |     | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |     | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |     | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |     | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |-ParenExpr  'int'
      |   |   |   |   |     | | |   | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |     | | |   | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |-ParenExpr  'int'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |-ParenExpr  'int'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | | | | |-IntegerLiteral  'int' 1
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |     | | |   | | | |   | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | | |   | | | | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   | | | |   | | |   | | | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   | | | |   | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |     | | |   | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |     | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |     | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |     | | `-IntegerLiteral  'int' 2
      |   |   |   |   |     | `-IntegerLiteral  'int' 2
      |   |   |   |   |     `-IntegerLiteral  'int' 2
      |   |   |   |   |-CompoundStmt 
      |   |   |   |   | `-IfStmt  has_else
      |   |   |   |   |   |-BinaryOperator  'int' '=='
      |   |   |   |   |   | |-ParenExpr  'unsigned int'
      |   |   |   |   |   | | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   | |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   | |   |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |   |   |   |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |   |   |       |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |   |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   | |   |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   | |   |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |   |       |   |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |   |       |       |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |   |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   | |   |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   | |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   |   |   |   |   | |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   | |       |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |       |   |   |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |       |   |       |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |       |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   | |       |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   | |       |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |       |       |   |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   | |       |       |       |   `-IntegerLiteral  'int' 5
      |   |   |   |   |   | |       |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   | |       |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   | |       `-IntegerLiteral  'int' 5
      |   |   |   |   |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   |   |   |   |   `-BinaryOperator  'int' '*'
      |   |   |   |   |   |     |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |-ParenExpr  'int'
      |   |   |   |   |   |     | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |     | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |-ParenExpr  'int'
      |   |   |   |   |   |     | |   | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |     | |   | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |-ParenExpr  'int'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |-ParenExpr  'int'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |-ParenExpr  'int'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | | | | |-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | | | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |     | |   | | | | |   | | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | |   | | | | |   | | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |     | |   | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |     | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |     | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |     `-IntegerLiteral  'int' 2
      |   |   |   |   |   |-CompoundStmt 
      |   |   |   |   |   | `-IfStmt  has_else
      |   |   |   |   |   |   |-BinaryOperator  'int' '=='
      |   |   |   |   |   |   | |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   | |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   | |   |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |   |   |   |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |   |   |       |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |   |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   | |   |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   |   | |   |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |   |       |   |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |   |       |       |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |   |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   | |   |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   |   | |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   |   |   |   |   |   | |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   | |       |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |       |   |   |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |       |   |       |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |       |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   | |       |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   |   | |       |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |       |       |   |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   | |       |       |       |   `-IntegerLiteral  'int' 6
      |   |   |   |   |   |   | |       |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   | |       |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   |   | |       `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   |   |   |   |   |   `-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | |   | | | |   | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   | | | |   | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | | | | |-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |     | |   | | | |   | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | |   | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |     | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |     | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |     | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |     `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |-CompoundStmt 
      |   |   |   |   |   |   | `-IfStmt  has_else
      |   |   |   |   |   |   |   |-BinaryOperator  'int' '=='
      |   |   |   |   |   |   |   | |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   | |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   | |   |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |   |   |   |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |   |   |       |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |   |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   | |   |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   |   |   | |   |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |   |       |   |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |   |       |       |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |   |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   | |   |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   |   |   | |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   |   |   |   |   |   |   | |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   | |       |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |       |   |   |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |       |   |       |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |       |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   | |       |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   |   |   | |       |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |       |       |   |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   | |       |       |       |   `-IntegerLiteral  'int' 7
      |   |   |   |   |   |   |   | |       |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   | |       |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   |   |   | |       `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   |   |   |   |   |   |   `-ParenExpr  'int'
      |   |   |   |   |   |   |   |     `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | | | | |-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |       | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | | |   | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |   |       | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |       | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |       | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |       | `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |   |       `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |-CompoundStmt 
      |   |   |   |   |   |   |   | `-IfStmt  has_else
      |   |   |   |   |   |   |   |   |-BinaryOperator  'int' '=='
      |   |   |   |   |   |   |   |   | |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   |   | |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   |   | |   |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |   |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   |   | |   |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |   |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |   |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |   |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |   |   |   |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |   |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   |   | |   |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   |   | |   |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |   |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |   |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |   |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |   |   |       |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |   |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   |   | |   |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |   |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   |   |   |   | |   |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |   |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   |   | |   |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |   |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |   |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |   |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |   |       |   |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |   |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   |   | |   |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   |   | |   |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |   |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |   |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |   |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |   |       |       |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |   |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   |   | |   |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   |   |   |   | |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |     `-BinaryOperator  'unsigned int' '<<'
      |   |   |   |   |   |   |   |   | |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   |   | |       |   |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |       |   | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   |   | |       |   |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |       |   |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |       |   |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |       |   |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |       |   |   |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |       |   |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   |   | |       |   |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   |   | |       |   |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |       |   |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |       |   |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |       |   |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |       |   |       |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |       |   |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   |   | |       |   `-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |       |     `-BinaryOperator  'unsigned int' '>>'
      |   |   |   |   |   |   |   |   | |       |       |-ParenExpr  'unsigned int'
      |   |   |   |   |   |   |   |   | |       |       | `-BinaryOperator  'unsigned int' '^'
      |   |   |   |   |   |   |   |   | |       |       |   |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |       |       |   | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |       |       |   |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |       |       |   |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |       |       |   |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |       |       |   `-ParenExpr  'uint32_t':'unsigned int'
      |   |   |   |   |   |   |   |   | |       |       |     `-BinaryOperator  'uint32_t':'unsigned int' '<<'
      |   |   |   |   |   |   |   |   | |       |       |       |-ImplicitCastExpr  'uint32_t':'unsigned int' <LValueToRValue>
      |   |   |   |   |   |   |   |   | |       |       |       | `-ArraySubscriptExpr  'uint32_t':'unsigned int' lvalue
      |   |   |   |   |   |   |   |   | |       |       |       |   |-ImplicitCastExpr  'uint32_t *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |       |       |       |   | `-DeclRefExpr  'uint32_t [20]' lvalue Var 0x55f4f65fd298 'input_str' 'uint32_t [20]'
      |   |   |   |   |   |   |   |   | |       |       |       |   `-IntegerLiteral  'int' 8
      |   |   |   |   |   |   |   |   | |       |       |       `-IntegerLiteral  'int' 13
      |   |   |   |   |   |   |   |   | |       |       `-IntegerLiteral  'int' 17
      |   |   |   |   |   |   |   |   | |       `-IntegerLiteral  'int' 5
      |   |   |   |   |   |   |   |   | `-ImplicitCastExpr  'unsigned int' <IntegralCast>
      |   |   |   |   |   |   |   |   |   `-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |     `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |       | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | |-ParenExpr  'int'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | | `-BinaryOperator  'int' '+'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | |   |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | |   | |-BinaryOperator  'int' '*'
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | |   | | |-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   | `-IntegerLiteral  'int' 3
      |   |   |   |   |   |   |   |   |       | |   | | | | | | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | |   | | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       | |   `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |       | `-IntegerLiteral  'int' 2
      |   |   |   |   |   |   |   |   |       `-IntegerLiteral  'int' 1
      |   |   |   |   |   |   |   |   |-CompoundStmt 
      |   |   |   |   |   |   |   |   | |-CallExpr  'int'
      |   |   |   |   |   |   |   |   | | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |   |   |   |   |   |   |   | | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |   |   |   |   |   |   |   | | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |   |   |   |   |   |   |   | |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |   | |     `-StringLiteral  'char [5]' lvalue "Wow!"
      |   |   |   |   |   |   |   |   | `-ReturnStmt 
      |   |   |   |   |   |   |   |   `-CompoundStmt 
      |   |   |   |   |   |   |   |     |-CallExpr  'int'
      |   |   |   |   |   |   |   |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |   |   |   |   |   |   |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |   |   |   |   |   |   |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |   |   |   |   |   |   |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |   |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |   |   |   |   |   |   |   |     `-ReturnStmt 
      |   |   |   |   |   |   |   `-CompoundStmt 
      |   |   |   |   |   |   |     |-CallExpr  'int'
      |   |   |   |   |   |   |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |   |   |   |   |   |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |   |   |   |   |   |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |   |   |   |   |   |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |   |   |   |   |   |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |   |   |   |   |   |   |     `-ReturnStmt 
      |   |   |   |   |   |   `-CompoundStmt 
      |   |   |   |   |   |     |-CallExpr  'int'
      |   |   |   |   |   |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |   |   |   |   |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |   |   |   |   |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |   |   |   |   |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |   |   |   |   |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |   |   |   |   |   |     `-ReturnStmt 
      |   |   |   |   |   `-CompoundStmt 
      |   |   |   |   |     |-CallExpr  'int'
      |   |   |   |   |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |   |   |   |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |   |   |   |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |   |   |   |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |   |   |   |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |   |   |   |   |     `-ReturnStmt 
      |   |   |   |   `-CompoundStmt 
      |   |   |   |     |-CallExpr  'int'
      |   |   |   |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |   |   |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |   |   |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |   |   |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |   |   |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |   |   |   |     `-ReturnStmt 
      |   |   |   `-CompoundStmt 
      |   |   |     |-CallExpr  'int'
      |   |   |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |   |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |   |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |   |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |   |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |   |   |     `-ReturnStmt 
      |   |   `-CompoundStmt 
      |   |     |-CallExpr  'int'
      |   |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |   |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |   |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |   |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |   |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |   |     `-ReturnStmt 
      |   `-CompoundStmt 
      |     |-CallExpr  'int'
      |     | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
      |     | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
      |     | `-ImplicitCastExpr  'const char *' <NoOp>
      |     |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
      |     |     `-StringLiteral  'char [4]' lvalue "Ow!"
      |     `-ReturnStmt 
      `-CompoundStmt 
        |-CallExpr  'int'
        | |-ImplicitCastExpr  'int (*)(const char *)' <FunctionToPointerDecay>
        | | `-DeclRefExpr  'int (const char *)' Function 0x55f4f6587120 'puts' 'int (const char *)'
        | `-ImplicitCastExpr  'const char *' <NoOp>
        |   `-ImplicitCastExpr  'char *' <ArrayToPointerDecay>
        |     `-StringLiteral  'char [4]' lvalue "Ow!"
        `-ReturnStmt 
"""

f = open("out.txt", "r")
ast = f.read()
f.close()
for line in ast.splitlines():
    if "main" in line:
        ast = ast[ast.index(line):]
        break
ast = re.sub(r"0x5.*?>", "", ast)
ast = re.sub(r"\[.*?m", "", ast)

# print ast

BinaryOperator_map = {
    "==":   0,
    "<<":   1,
    ">>":   2,
    "^":    3,
    "+":    4,
    "-":    5,
    "*":    6,
    "&&":   7,
    "<":    8,
    "=":    9,
}

ArraySubscriptExpr_map = {
    "uint32_t": 4,
}

sym_map = {
    "memset":   0,
    "scanf":    1,
    "puts":     2,
}


# we need manually setup var size
sym_size = {
    "input_str": 80,
    "res"      : 4,
    "i"        : 4,
}

node_list = []


def find_addr(line):
    l = line.split()
    for s in l:
        if "0x5" in s:
            return l.index(s)
def find_pattern(pattern, line):
    line = line[line.index("-")+1:]
    return line.split()[line.split().index(pattern) + 1].replace("\'", "")

def parse_node(line_num):
    line = ast.splitlines()[line_num]
    curr_idx = line.index("-")
    kind = line[curr_idx+1:].split()[0]

    curr_node = {}
    curr_node["kind"] = kind
    curr_node["childsize"] = 0
    curr_node["child"] = []
    curr_node["value"] = None
    curr_node["var_id"] = None

    if kind == "VarDecl":
        l = line.split()
        var_name = l[l.index("used")+1]
        if var_name in sym_map:
            var_id = sym_map[var_name]
        else:
            var_id = len(sym_map)
            sym_map[var_name] = var_id

        curr_node["value"] = sym_size[var_name]
        curr_node["var_id"] = var_id
    elif kind == "DeclRefExpr":
        var_name = line.split()[find_addr(line) + 1].replace("\'", "")
        var_id = sym_map[var_name]

        curr_node["var_id"] = var_id
    elif kind == "IntegerLiteral":
        curr_node["value"] = line.split()[-1]
    elif kind == "BinaryOperator":
        curr_node["value"] = BinaryOperator_map[line.split()[-1].replace("\'", "")]
    elif kind == "ArraySubscriptExpr":
        curr_node["value"] = ArraySubscriptExpr_map[find_pattern("ArraySubscriptExpr", line).split(":")[0]]
    elif kind == "StringLiteral":
        ss = find_pattern("lvalue", line)
        if ss in sym_map:
            var_id = sym_map[ss]
        else:
            var_id = len(sym_map)
            sym_map[ss] = var_id
        curr_node["var_id"] = var_id
    elif kind == "ImplicitCastExpr":
        # dereference pointer
        if "LValueToRValue" in line:
            curr_node["value"] = 1
            curr_node["var_id"] = ArraySubscriptExpr_map[find_pattern("ImplicitCastExpr", line).split(":")[0]]
        else:
            curr_node["value"] = 0
    elif kind == "<<<NULL>>>":
        kind = "NULLLL"
        curr_node["kind"] = kind

    # print line[line.index("-")+1:]
    # print curr_node
    # print ""
    node_list.append(curr_node)

    child_line_num = line_num + 1
    while True:
        if child_line_num >= len(ast.splitlines()):
            break
        next_line = ast.splitlines()[child_line_num]
        next_idx = next_line.index("-")
        if next_idx <= curr_idx:
            break
        next_node, child_line_num = parse_node(child_line_num)
        curr_node["childsize"] += 1
        curr_node["child"].append(next_node)

    return curr_node, child_line_num


root = parse_node(0)




def dump_to_code(root):
    # setup init_DeclRef


    # setup code
    bss_node = []
    init_node = []
    malloc_node = []
    tmp_list = range(len(node_list))
    random.shuffle(tmp_list)
    for i in tmp_list:
        bss_node.append("struct node node%d;" %i)

    for i in range(len(node_list)):
        node = node_list[i]
        if node["value"]:
            init_node.append("node%d.value = %s;" % (i, node["value"]))
        if node["var_id"]:
            init_node.append("node%d.var_id = %s;" % (i, node["var_id"]))
        init_node.append("node%d.func = %s;" % (i, node["kind"]))

        if node["childsize"] == 0:
            continue

        init_node.append("node%d.childsize = %d;" % (i, node["childsize"]))
        malloc_node.append("node%d.child = (struct node **)malloc(%d*sizeof(struct node*));" % (i, node["childsize"]))

        for j in node["child"]:
            child_idx = node_list.index(j)
            init_node.append("node%d.child[%d] = &node%d;" % (i, node["child"].index(j), child_idx))



    print "\n".join(bss_node)
    print ""

    # obfuscate init_node_func
    def randomlist(l):
        ll = []
        length = len(l)
        for _ in range(length):
            r = random.randint(0, length - _ - 1)
            ll.append(l[r])
            l.remove(l[r])
        assert len(ll) == length
        return ll

    malloc_node = randomlist(malloc_node)
    init_node = randomlist(init_node)

    init_node_func = "__attribute__((constructor))\nvoid init_node() {\n%s\n%s\n}" % ("\n".join(malloc_node), "\n".join(init_node))
    print init_node_func

    pass


dump_to_code(root)

# for s in sym_map:
#     print "\tDeclRef[%d] = (void *) %s;" % (sym_map[s], s)

# flag = "flag{HEY!Lumpy!!W@tcH_0ut_My_TrEe!!}"
# import pwn
# a = []
# for i in range(9):
#     a.append(pwn.u32(flag[4*i:4*i+4]))
# print a

def dfs(n):
    expr = ""
    while True:
        f = True
        for i in range(2, 6):
            if n % i == 0:
                expr += "*%d" % i
                n = n/i
                f = False
                break
        if f:
            break
        if n == 1:
            return "1" + expr
    ret = dfs(n-1)
    expr = "(" + ret + " + 1)" + expr

    return expr

def obfnum(n):
    expr = dfs(n)
    assert n == eval(expr)
    return expr

# print obfnum(0xa25dc66a)
# print obfnum(0x00aa0036)
# print obfnum(0xc64e001a)
# print obfnum(0x369d0854)
# print obfnum(0xf15bcf8f)
# print obfnum(0x6bbe1965)
# print obfnum(0x1966cd91)
# print obfnum(0xd4c5fbfd)
# print obfnum(0xb04a9b1b)

# print obfnum(0xAAAAAAAA)