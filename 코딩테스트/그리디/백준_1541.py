# 백준 1541
# 잃어버린 괄호

data =input().split("-")     # 굳이 list로 안해도 split있으면 list로 나옴

result=0

for i in data[0].split("+"):    #이거 처음에 그냥 result+=int(data[0])으로 했는데 런타임 에러 나왔는데 이유는 잘 모르겠음.. 
    result+=int(i)
for i in data[1:]:
  for j in i.split('+'):
    result-=int(j)
print(result)

