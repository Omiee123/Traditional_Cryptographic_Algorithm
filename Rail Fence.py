#!/usr/bin/env python
# coding: utf-8

# In[13]:


def process(text):
    
    #Removing Spaces between words
    text = text.replace(" ","")
    print("String after removing spaces between words : {}".format(text))
    
    #Making String of Even Length
    rem = len(text)%len(key)
    if rem != 0:
        text += "x"*(len(key)-rem)
        
    print("String after making it of even length : {}".format(text))
    print()
    
    return text


# In[14]:


def encrypt_decrypt(string,key):
    
    string_key = len(key)
    string = process(string)
    string_len = len(string)
    
    cipher_matrix = [[None]*string_key for i in range(int(string_len/string_key))]
    k=0
    for i in range(int(string_len/string_key)):
        for j in range(string_key):
            cipher_matrix[i][j] = string[k]
            k+=1
        
    result = ""

    for i in range(string_key):
        temp = int(key[i])-1
        for j in range(int(string_len/string_key)):
            result = result + cipher_matrix[j][temp]
            
    return result


# In[15]:


def read_text():
    print("Enter the plain text")
    text = input()
    return text


# In[16]:


def read_key():
    print("Enter the key Message")
    key = input()
    return key


# In[18]:


string = read_text()
key=read_key()
result = encrypt_decrypt(string,key)
print(result)


# In[ ]:




