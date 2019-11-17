#!/usr/bin/env python
# coding: utf-8

def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
            
    return result

def decrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + (26-s) - 65) % 26 + 65)
        else:
            result += chr((ord(char) + (26-s) - 97) % 26 + 97)
            
    return result

def encrypt_decrypt(text,s,input_var):
    result = ""
    s = s if input_var == 1 else (26-s)
    
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
            
    return result

print("Press the suitable number")
print("1. Encrypt Plain Text")
print("2. Decrypt Encrypted Text")
input_var = int(input())

if input_var == 1:
    print("Enter Plain Text")
    text = input()
    print("Enter key")
    s = int(input())
    result = encrypt_decrypt(text,s,input_var)
    #result = encrypt(text,s)
    print(result)
    
if input_var == 2:
    print("Enter Encrypted Text")
    text = input()
    print("Enter key")
    s = int(input())
    result = encrypt_decrypt(text,s,input_var)
    #decrypt(text,s)
    print(result)
