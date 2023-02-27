def printTriangle(N):
  # Code here
  for i in range(N):
    for j in range(N-i):
      print('*',end=' ')
    print()


if __name__=="__main__":
  N=5
  printTriangle(N)