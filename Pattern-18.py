def printTriangle(N):
  # Code here
  for i in range(1,N+1):
    for j in range(i):
      print(chr(65+(N-1-j)),end=' ')
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)