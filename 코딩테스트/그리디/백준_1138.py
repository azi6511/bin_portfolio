# -*- coding: utf-8 -*-
"""백준 1138.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Tn5wYBfmcIGY-Xsa8rw1F1PjgKHpGEs
"""

# 백준 1138
# 한 줄로 서기

import sys
input = sys.stdin.readline

N = int(input())
back = list(map(int,input().split()))
result=[0]*N

for i in range(1,N+1):
  cnt= 0
  temp=back[i-1]
  for j in range(len(result)):
    if temp==cnt and result[j]==0:
      result[j]=i
      break
    elif result[j]==0:
      cnt+=1

print(*result)

