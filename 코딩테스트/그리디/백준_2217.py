# -*- coding: utf-8 -*-
"""백준 2217.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Tn5wYBfmcIGY-Xsa8rw1F1PjgKHpGEs
"""

N = int(input())
k=[]
for i in range(N):
  weight=int(input())
  k.append(weight)

k.sort(reverse=True)

a=[]
for i in range(len(k)):
  a.append(k[i]*(i+1))
  
print(max(a))