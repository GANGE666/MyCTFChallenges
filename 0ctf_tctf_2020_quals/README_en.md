# 0CTF/TCTF 2020 Quals Happy Tree WriteUp

- [中文](./README.md)

### Overview

Rev, 17 solves, 407 points

The insight of this challenge is virtual machine of AST (Abstract Syntax Tree). The original execution logic hide behind the interpretation of AST node.

## Intended Solution

After recognized this challenge is obfuscate by the interpretation of AST, you can analyze the AST node and obtain the pseudo code of the verification logic. Then write a decryption algorithm to obtain the flag.

