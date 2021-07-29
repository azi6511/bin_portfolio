# 백준 2217
# 로프

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
