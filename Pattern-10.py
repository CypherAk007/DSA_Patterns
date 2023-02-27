def printTriangle(N):
  # Code here
  for i in range(1,N*2):
    stars=i
    if i>N:
      stars=2*N-i
    for j in range(stars):
      print('*',end=' ')
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)
                