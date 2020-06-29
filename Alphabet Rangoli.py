def print_rangoli(size):
    for i in range(1,n+1):
        s=[]
        for j in range(0,n):  
            if(j<i):
                s.append(chr(97+n-(i-j)))
        s="".join(s)
        x=[x for x in s[1:] ]
        x="".join(x)[::-1]
        print("-".join(x+s).center(4*n-3 , "-"))

    for i in range(1,n):
        s=[]
        for j in range(0,n):  
            if(j>=i):
              s.append(chr(97+j))         
        s="".join(s)
        x=[x for x in s[1:] ]
        x="".join(x)[::-1]
        print("-".join(x+s).center(4*n-3 , "-"))    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
