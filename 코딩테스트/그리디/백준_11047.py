#백준 11047
#동전 0

n, k = map(int, input().split())
number=[]
count=0
for i in range(n):
  a =int(input())
  number.append(a)

number.sort(reverse=True)
for i in range(len(number)):
  count += (k//number[i])
  k %= number[i]

print(count)
