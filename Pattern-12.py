
def printTriangle(N):
  # Code here
  for i in range(1,N+1):
    # Num
    for j in range(1,i+1):
      print(j,end=' ')
    
    # space
    val=4*(N-i)
    for j in range(val):
      print(' ',end='')
        
    # revNum
    for j in range(i,0,-1):
      print(j,end=' ')
        
    print()


if __name__=="__main__":
  N=5
  printTriangle(N)
            
