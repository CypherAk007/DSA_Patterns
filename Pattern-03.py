def printTriangle(N):
  for i in range(0,N): 
    for j in range(i+1): 
      print(j+1,end=' ')
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)