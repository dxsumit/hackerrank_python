x=int(input())
y=int(input())
z=int(input())

N=int(input())

A=[i for i in range(0,x+1)]
B=[i for i in range(0,y+1)]
C=[i for i in range(0,z+1)]
list=[[a,b,c] for a in A for b in B for c in C if(a+b+c !=N)]

print(list)
