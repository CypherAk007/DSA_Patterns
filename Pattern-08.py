def printTriangle(N):
  # Code here
  for i in range(N):
    # space
    for j in range(i):
      print(' ',end='')
    # star
    for j in range(0,2*(N-1-i)+1):
      print('*',end='')
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)