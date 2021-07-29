#백준 11399
#ATM

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

#예약어 쓰지 말자(sum같은거!)
