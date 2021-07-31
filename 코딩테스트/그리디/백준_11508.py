# 백준 11508
# 2+1 세일

N = int(input())

product=[]
result = 0

for i in range(N):
  sample=int(input())
  product.append(sample)

product.sort(reverse=True)
other= product[2::3]

result+=sum(product)-sum(other)
  
print(result)


#시간이 넘 오래 
