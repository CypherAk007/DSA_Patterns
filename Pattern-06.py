def printTriangle(N):
  # Code here
  for i in range(N):
    for j in range(1,N+1-i):
      print(j,end=' ')
    print()


if __name__=="__main__":
  N=5
  printTriangle(N)