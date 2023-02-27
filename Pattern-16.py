def printTriangle(N):
  # Code here
  val=65
  for i in range(0,N):
    for j in range(i+1):
      print(chr(val+i),end='')
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)