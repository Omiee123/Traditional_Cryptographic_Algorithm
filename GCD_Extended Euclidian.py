#!/usr/bin/env python
# coding: utf-8

def gcdExtended(x, y):
    #variable Intialisation
    a1,b1 = 1,0
    a2,b2 = 0,1
    a3,b3 = (x,y) if x > y else (y,x)
    
    large = a3
    gcd = 0
    print(a1,a2,a3,b1,b2,b3)
    while b3 != 1:
        div = int(a3/b3)
        print("div = {}".format(div))
        t1 = a1 - (div * b1)
        t2 = a2 - (div * b2)
        t3 = a3 - (div * b3)
        if t3==0:
            gcd=b3
            break
        
        a1,a2,a3 = b1,b2,b3
        b1,b2,b3 = t1,t2,t3
        print(a1,a2,a3,b1,b2,b3)
        
    if gcd == 0:
        gcd = b2 if b2 > 0 else (large+b2)
        
    return gcd

a = int(input("Enter First number :"))
b = int(input("Enter Second number :"))
g = gcdExtended(a, b)
print("GCD of Two number using Extednded Euclidean is : {}".format(g))
