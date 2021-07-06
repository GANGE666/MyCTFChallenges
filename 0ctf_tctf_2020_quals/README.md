# 0CTF/TCTF 2020 Quals Happy Tree WriteUp

- [English](./README_en.md)

### 概述

Rev, 17 solves, 407 points

本题的出题思路为AST(Abstract Syntax Tree) 虚拟机，即通过对AST节点的解释执行以隐藏原本执行逻辑。

### 预期解法

选手识别出本题的混淆方式为对AST的解释执行后，编写代码解析AST节点，得到校验逻辑的伪代码，并分析其中的逻辑，编写解密算法获取flag。

