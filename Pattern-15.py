def printTriangle(N):
  # Code here
  for i in range(N,0,-1):
    val=65
    for j in range(i):
      print(chr(val+j),end='')
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)