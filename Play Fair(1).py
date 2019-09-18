#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Unique_key(plain_text, key):
    
    Unique_key = ""
       
    for i in range(0,len(key)):

        d=0
        for j in range(0,i):
            if (key[i] == key[j]):
                d = 1
                break

        if(d==0):
            Unique_key += key[i]

    return Unique_key


# In[2]:


def key_encrypt(text,s):
    #variable Exchange
    plain_text = text
    key = s
    
    #Initializing Key_Matrix
    Key_Matrix = [[None]*5 for j in range(5)]
    
    #Identifying Unique Alphabets from
    jerry = Unique_key(text,s)
    print("Unique Alphabets from Key {}".format(jerry))
    print()
    
    #Convert Unique Character to ASCII Array
    ascii_array = [ ord(i) for i in jerry]
    
    #Filling Unique Character to Key_Matrix
    i=j=k=0
    while i != len(jerry):
        if j == 5:
            k=k+1
            j=0
        else:
            Key_Matrix[k][j]=jerry[i]
            j=j+1
            i=i+1
    
    #Filling Rest of Matrix
    alpha_code = 97
    for k in range(5):
        for j in range(5):
            if Key_Matrix[k][j] == None :
                if alpha_code in ascii_array:
                    while alpha_code in ascii_array:
                        alpha_code = alpha_code + 1

                Key_Matrix[k][j] = chr(alpha_code)
                if alpha_code == 105:
                    alpha_code = alpha_code + 2
                else:
                    alpha_code = alpha_code + 1
        
    return Key_Matrix


# In[3]:


def find_char(Matrix,letter):
    
    for i in range(5):
        for j in range(5):
            if Matrix[i][j] == letter:
                return i,j


# In[11]:


def encrypt(text,s):
    
    #Finding Key_Matrix
    Key_Matrix = key_encrypt(text,s)
    print("Key Matrix For the Given Key is : ")
    print(Key_Matrix)
    print()
    
    #Removing Spaces between words
    text = text.replace(" ","")
    print("String after removing spaces between words : {}".format(text))
            
    #Removing two adjacent same character
    for i in range(len(text)-1):
        if text[i] == text[i+1] and i%2 == 0:
            #text.insert(i+1,'x')
            text_a = text[0:i+1]
            text_b = text[i+1:len(text)]
            text = text_a + "x" + text_b
            
    print("String after removing same adjacent Character : {}".format(text))
    print()
    
    #Making String of Even Length
    if len(text)%2 != 0:
        text += "x"
        
    print("String after making it of even length : {}".format(text))
    print()
    
    #Encryption
    answer = ""
    for i in range(0,len(text),2):
        #find i and i+1 in Key_Matrix
        char_1_i, char_1_j = find_char(Key_Matrix,text[i])
        char_2_i, char_2_j = find_char(Key_Matrix,text[i+1])
        
        #find Corresponding Encrypted Text
        if char_1_i != char_2_i and char_1_j != char_2_j:
            char_1 = Key_Matrix[char_1_i][char_2_j]
            char_2 = Key_Matrix[char_2_i][char_1_j]
            
        if char_1_i == char_2_i:
            char_1 = Key_Matrix[char_1_i][(char_1_j+1)%4]
            char_2 = Key_Matrix[char_2_i][(char_2_j+1)%4]
            
        if char_1_j == char_2_j:
            char_1 = Key_Matrix[(char_1_i+1)%4][char_1_j]
            char_2 = Key_Matrix[(char_2_i+1)%4][char_2_j]
        
        #Iterate with increment
        answer = answer + char_1 + char_2
        
    return answer


# In[12]:


def dec_encrypt(text,s):
    
    #Finding Key_Matrix
    Key_Matrix = key_encrypt(text,s)
    print("Key Matrix For the Given Key is : ")
    print(Key_Matrix)
    print()
       
    #Decryption
    answer = ""
    for i in range(0,len(text),2):
        #find i and i+1 in Key_Matrix
        char_1_i, char_1_j = find_char(Key_Matrix,text[i])
        char_2_i, char_2_j = find_char(Key_Matrix,text[i+1])
        
        #find Corresponding Encrypted Text
        if char_1_i != char_2_i and char_1_j != char_2_j:
            char_1 = Key_Matrix[char_1_i][char_2_j]
            char_2 = Key_Matrix[char_2_i][char_1_j]
            
        if char_1_i == char_2_i:
            char_1 = Key_Matrix[char_1_i][(char_1_j-1)%4]
            char_2 = Key_Matrix[char_2_i][(char_2_j-1)%4]
            
        if char_1_j == char_2_j:
            char_1 = Key_Matrix[(char_1_i-1)%4][char_1_j]
            char_2 = Key_Matrix[(char_2_i-1)%4][char_2_j]
        
        #Iterate with increment
        answer = answer + char_1 + char_2
        
    return answer


# In[14]:


print("Press the suitable number")
print("1. Encrypt Plain Text")
print("2. Decrypt Encrypted Text")
print()

input_var = int(input())
print()

if input_var == 1:
    print("Enter Plain Text")
    text = input()
    text = text.lower()
    print()

    print("Enter key")
    s = input()
    s = s.lower()
    print()

    result = encrypt(text,s)
    print("Encrypted Text : {}".format(result))
    
if input_var == 2:
    print("Enter Cipher Text")
    cipher_text = input()
    cipher_text = cipher_text.lower()
    print()
    
    if (len(cipher_text)%2) != 0:
        print("Cipher Text of Play Fair can not be of odd length")

    print("Enter key")
    dec_s = input()
    dec_s = dec_s.lower()
    print()

    result = dec_encrypt(cipher_text,dec_s)
    print("Encrypted Text : {}".format(result))


# 
