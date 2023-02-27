def printSquare(N):
  for i in range(N):
    for j in range(N):
      print('*',end=' ')
    print()

if __name__=="__main__":
  N=5
  printSquare(N)