# 0CTF/TCTF 2021 Quals FEA WriteUp

- [中文](./README.md)



### Overview

Rev, 14 solves, 458 points

This challenge implements a simple unpacking program. The hardened unpacking program will use  fastlz algorithm to decompress the shellcode and execute it. The shellcode requires players to provide an 8 bytes input, and compare with a solid ciphertext after a single round of IDEA encryption. (The ciphertext is calculated by a large number of randomly generated constants)

This challenge hopes to examine the players' ability to de-obfuscation and **Automatic Exploit Generation**. A large number of anti-debugging methods (time detection, breakpoint detection, a large number of int 3, etc.) and a variety of randomly generated obfuscation pattern have been added to the challenge. Unlike the previous AEG reverse challenges, players could not extract the ciphertext directly through a large number of heuristic methods. Players need to obtain key data(target ciphertext) in this challenge through simulation execution, hook or patch binary. And players need to solve this challenge 3 times within 10*3 seconds to prove the performance and reliability of their solutions.



### Intended Solution

Analysis process:

- After passing POW, the server will generate a binary and return it as base64
- [unpacker de-obfuscation] There is a slight control flow flattening. You can directly analyze or use various unflattening tools to de-obfuscate.
- In the unpacker, you could found anti-debugging, int 3 signal handler registered, decompressed and executed a shellcode.
- [Unpacking] Dump the executed shellcode, or statically analyze the decompression algorithm, or find the [decompression algorithm source code](https://github.com/ariya/FastLZ/blob/master/fastlz.c). Get the executed shellcode and enter the next step of analysis.
- [shellcode de-obfuscation] Dound several pattern to smash control flow (against IDA static analysis), and a large number of int 3 (int 3 has a handler registered in the unpacker).
- [Shellcode analysis] Recognize that the encryption algorithm is a single round IDEA, and extracte the round key. The target ciphertext is generated by a huge function.
- [Processing ideas] Use simulation execution to get the ciphertext, and write IDEA single round decryption script to complete the decryption.

Solving process:

- [Get binary] Decode base64

- [Extract shellcode] Use fastlz decompression/patch binary/dump to obtain shellcode

- [Decryption algorithm] IDEA single-round decryption, calculate the reverse round key.

- [Extract ciphertext] Use unicorn and other tools to simulate execution, set hook for int 3, and get ciphertext

- Decrypt the ciphertext to get the input and repeat three times to get the flag



### Deployment

```
cd deployment
unzip fea.zip
cd fea
docker-compose up -d --build
```



### Solution

```
cd solver
python3 solver.py
```

