# -*- coding: utf-8 -*-
"""백준 11399.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Tn5wYBfmcIGY-Xsa8rw1F1PjgKHpGEs
"""

N = int(input())
s = list(map(int,input().split()))
s.sort()
total=0
total_list=[]
for i in range(len(s)):
  total=total+s[i]
  total_list.append(total)

result=sum(total_list)
print(result)

