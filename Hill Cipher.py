#!/usr/bin/env python
# coding: utf-8

# In[1]:


def matrix_multi(mat1,mat2,row1,column1,column2):
    temp = [[0]*column2 for i in range(row1)]
    
    for i in range(row1):
        for j in range(column2):
            for k in range(column1):
                temp[i][j]=temp[i][j] + (mat1[i][k]*mat2[k][j])

    return temp


# In[2]:


def readmatrix():
    
    print("Enter the length of row and column")
    row = int(input())
    array = [ [0]*row for i in range(row) ]
    
    for i in range(row):
        array[i] = [ int(i) for i in input().split() ]
        
    return array


# In[3]:


def process(text):
    
    #Removing Spaces between words
    text = text.replace(" ","")
    print("String after removing spaces between words : {}".format(text))
    
    #Making String of Even Length
    rem = len(text)%len(key_matrix[0])
    if rem != 0:
        text += "x"*(len(key_matrix[0])-rem)
        
    print("String after making it of even length : {}".format(text))
    print()
    
    return text


# In[4]:


def encrypt(key_matrix,text):
    
    #Encryption
    answer = ""
    
    #Intializing empty matrix
    result=[[0]*1 for i in range(len(key_matrix[0]))]
    result_encry=result
    
    for i in range(0,len(text_final),len(key_matrix)):
        counter = 0

        #pushing chunk equal to length of key matrix
        while counter != len(key_matrix[0]):
            result[counter][0] = ord(text_final[i])-97
            counter = counter + 1
            i = i + 1
        
        #multiplying chunk with key_matrix
        result_encry = matrix_multi(key_matrix,result,len(key_matrix[0]),len(key_matrix),1)

        counter = 0
        
        #converting chunk to string and storing it in answer
        while counter != len(key_matrix[0]):
            answer += str(chr((result_encry[counter][0]%26)+97))
            counter = counter + 1
        
    return answer 


# In[5]:


print("Press the suitable number")
print("1. Encrypt Plain Text")
print("2. Decrypt Encrypted Text")
print()

input_var = int(input())
print()

if input_var == 1:
    print("Enter key")
    key_matrix = readmatrix()
    print(key_matrix)
    
    print("Enter Plain Text")
    text = input()
    text_lower = text.lower()
    text_final = process(text_lower)
    print()    
    
    print("Cipher Text is : {}".format(encrypt(key_matrix,text_final)))
    


# In[ ]:




