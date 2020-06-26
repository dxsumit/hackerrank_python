list=[]
n=int(input())
doList=[input().split() for i in range(0,n)]

for i in range(0,n):
      if(doList[i][0]=="insert"):
          list.insert(int(doList[i][1]) , int(doList[i][2]))
          
      elif(doList[i][0]=="print"):
          print(list)
          
      elif(doList[i][0] =="remove"):
          list.remove(int(doList[i][1]))
          
      elif(doList[i][0]=="append"):
          list.append(int(doList[i][1]))
          
      elif(doList[i][0]=="sort"):
          list.sort()
          
      elif(doList[i][0]=="pop"):
          list.pop()
          
      elif(doList[i][0]=="reverse"):
          list.reverse()
