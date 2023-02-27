def printDiamond(N):
    # Code here
    topdown(N)
    bottomup(N)
    
    
def topdown(N):
    for i in range(1,N+1):
        # space
        for j in range(N-i):
            print(' ',end='')
        # star
        for j in range(i):
            print('*',end=' ')
        print()

def bottomup(N):
    for i in range(N):
        for j in range(i):
            print(' ',end='')
        for j in range(N-i):
            print('*',end=' ')
        print()
        
if __name__=="__main__":
  N=5
  printDiamond(N)