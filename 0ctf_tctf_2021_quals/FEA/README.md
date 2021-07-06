# 0CTF/TCTF 2021 Quals FEA WriteUp

- [English](./README_en.md)



### 概述

Rev, 14 solves, 458 points

本题实现了一个简单的脱壳程序，被加固后的壳程序会使用fastlz算法解压shellcode并执行。shellcode中要求选手提供一个8 bytes的输入，并将输入进行单轮IDEA加密后与密文进行比较。（密文通过大量随机生成的常量计算得到）

本题希望考察的是选手的对抗混淆及自动化解题的能力，题目中加入了大量的反调试手段（时间检测、断点检测、大量的int 3等）及多种随机生成的混淆方式。与之前的AEG逆向题目不同，本题没有办法直接通过大量的启发式方法提取关键数据，选手需要通过模拟执行、hook或patch binary等方式获取题目中的一些关键数据。并且选手需要在10s*3内完成三次挑战以证明其解法的性能及可靠性。



### 预期解法

 分析流程：

- 通过pow后，服务器会生成一个binary以base64形式返回
- [解混淆] 初步分析，发现有轻微的控制流平坦化，直接分析或使用各种去平坦化工具解混淆分析
- 发现其中部分反调试、注册了int 3的信号处理、解压一段shellcode并执行
- [脱壳] patch反调试dump出执行的shellcode，或静态分析解压算法，或找到[解压算法源码](https://github.com/ariya/FastLZ/blob/master/fastlz.c)。获取到所执行的shellcode进入下一步分析。
- [shellcode解混淆] 发现多种模式的混淆（对抗IDA静态分析）、及大量的int 3（int 3在壳中注册了处理函数），去除混淆
- [shellcode逻辑分析] 发现加密算法为单轮IDEA，提取出轮密钥。要求输入明文，发现密文被通过一个巨大的函数生成
- [处理思路] 利用模拟执行得到密文，编写IDEA单轮解密脚本完成解密。

解题流程：

- [获取binary] 解码base64
- [提取shellcode] 使用fastlz/patch 二进制等方式获取shellcode
- [编写解密算法] IDEA单轮加密，计算出常量轮密钥，求逆即可
- [提取密文] 使用unicorn等工具模拟执行，对int 3设置hook，得到密文
- 解密密文得到输入，重复三次，获取flag



### 环境部署

```
cd deployment
unzip fea.zip
cd fea
docker-compose up -d --build
```



### 解题脚本

```
cd solver
python3 solver.py
```

