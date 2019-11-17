#!/usr/bin/env python
# coding: utf-8

def encrypt_decrypt(text,key,input_var):
    result=""
    
    for i in range(len(text)):
        j=(i%len(key))

        char = text[i]
        
        s = (ord(key[j])-65) if key[j].isupper() else (ord(key[j])-97)
        s = s if input_var == 1 else (26-s)
        if (char.isupper()):
                result += chr((ord(char) + s -65) % 26 + 65)

        else:
                result += chr((ord(char) + s -97) % 26 + 97)
    
    return result

print("Press the suitable number")
print("1. Encrypt Plain Text")
print("2. Decrypt Encrypted Text")
input_var = int(input())

if input_var == 1:
    print("Enter Plain Text")
    text = input()
    print("Enter key")
    s = input()
    result = encrypt_decrypt(text,s,input_var)
    print(result)
    
if input_var == 2:
    print("Enter Encrypted Text")
    text = input()
    print("Enter key")
    s = input()
    result = encrypt_decrypt(text,s,input_var)
    print(result)
