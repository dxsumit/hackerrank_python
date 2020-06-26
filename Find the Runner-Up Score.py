n=int(input())

arr=list(map(int , input().split()))

if(len(arr)==n):
    arr1 =list(set(arr))
    arr1.sort()
    print(arr1[len(arr1)-2])
