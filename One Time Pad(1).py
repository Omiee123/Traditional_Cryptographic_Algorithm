#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[ ]:


print("Press the suitable number")
print("1. Encrypt Plain Text")
print("2. Decrypt Encrypted Text")
input_var = int(input())

def read_text(val):
    print("Enter "+val+" Text")
    text = input()
    return text

def read_key():
    print("Enter Key")
    s = input()
    return s

string = read_text("plain" if input_var == 1 else "cipher")
key = read_key()
    
while len(string) != len(key):
    print("Key and text should be of same length")
    key = read_key()
        
result = encrypt_decrypt(string,key,input_var)
print(result)


# In[ ]:




