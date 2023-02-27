def printTriangle(N):
  # Code here
  # 1st half
  c=0
  for i in range(N,0,-1):
    # star
    for j in range(i):
        print('*',end='')
    # space
    for j in range(c):
        print(' ',end='')
    # star
    for j in range(i):
        print('*',end='')
    c+=2
    print()
      
  # 2nd half
  c=2*(N-1)
  for i in range(1,N+1):
    # star
    for j in range(i):
        print('*',end='')
    # space
    for j in range(c):
        print(' ',end='')
    # star
    for j in range(i):
        print('*',end='')
    c-=2
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)
