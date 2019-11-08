#!/usr/bin/python3
from string import ascii_lowercase as lowercase
import subprocess


KEY = open("key.txt", 'r').read()
MSG = open("msg.txt" ,'r').read()
abc =dict()
flag = ''
for i in lowercase:
    abc[i] = ord(i) - ord('a')
for i in range(0, len(MSG)-1):
    M = abc[MSG[i]] 
    K = abc[KEY[i]]
    if (M - K) >= 0:
        flag += (chr(M - K + ord('a')))
    else:
        flag += (chr(26 - (K - M) + ord('a')))
flag = flag.upper()       
f = open('flag.txt', 'w+')
f.write("picoCTF{" + flag + "}\n")
