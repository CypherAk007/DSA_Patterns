def printTriangle(N):
  # Code here
  odd=1
  for i in range(N):
    # space
    for j in range(N-1-i):
        print('',end=' ')
    # star
    for k in range(2*i+1):
        print('*',end='')
    print()


if __name__=="__main__":
  N=5
  printTriangle(N)