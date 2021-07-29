"""백준 5585.ipynb

change = 1000-int(input())
count=0
coin =[500,100,50,10,5,1]

for i in range(len(coin)):
  count += (change//coin[i])
  change %= coin[i]

print(count)

