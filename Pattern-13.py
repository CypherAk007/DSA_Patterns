def printTriangle(N):
  # Code here
  c=1
  for i in range(1,N+1):
    for j in range(i):
      print(c,end=' ')
      c+=1
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)
            
