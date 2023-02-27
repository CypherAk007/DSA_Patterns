def printTriangle(N):
  # Code here
  for i in range(2*N-1):
    for j in range(2*N-1):
      top=i
      left=j
      right=((2*N)-1)-1-j
      bottom=((2*N)-1)-1-i
      print(N-min(top,left,right,bottom),end=' ')
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)