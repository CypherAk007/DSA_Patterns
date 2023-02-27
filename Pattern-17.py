def printTriangle(N):
  # Code here  
  for i in range(N):
    # space
    for j in range(N-i-1):
      print(' ',end='')
      
    # chr
    val=65
    nochr=2*i+1
    mid=(nochr//2)
    for j in range(nochr):
      if j<mid:
        print(chr(val),end='')
        val+=1
      else:
        print(chr(val),end='')
        val-=1
    print()


if __name__=="__main__":
  N=5
  printTriangle(N)