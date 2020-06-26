s=input()
x=list(map(lambda n: n.isalnum() , s))
print("True") if(x.count(True)>=1) else print("False")

x=list(map(lambda n: n.isalpha() , s))
print("True") if(x.count(True)>=1) else print("False")

x=list(map(lambda n: n.isdigit() , s))
print("True") if(x.count(True)>=1) else print("False")

x=list(map(lambda n: n.islower() , s))
print("True") if(x.count(True)>=1) else print("False")

x=list(map(lambda n: n.isupper() , s))
print("True") if(x.count(True)>=1) else print("False")
