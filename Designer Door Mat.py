N , M= input().split()
ctr=1
for i in range(int(N)//2):
  shape=ctr*".|."
  print(shape.center(int(M) , "-"))
  ctr+=2

print("WELCOME".center(int(M) , "-"))
ctr-=2

for i in range(int(N)//2):
  shape=ctr*".|."
  print(shape.center(int(M) , "-"))
  ctr-=2
