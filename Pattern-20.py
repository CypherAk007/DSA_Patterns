
def printTriangle(N):
  # Code here
  space=2*(N-1)
  for i in range(1,2*N):
    stars=i
    if i>N:
      stars=2*N-i
          
    # star
    for j in range(stars):
      print('*',end='')
        
    # space
    for j in range(space):
      print(' ',end='')

    if i>=N:
      space+=2
    else:
      space-=2

    # star
    for j in range(stars):
      print('*',end='')
    
    print()
            
if __name__=="__main__":
  N=5
  printTriangle(N)