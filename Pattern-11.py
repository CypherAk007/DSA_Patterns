def printTriangle(N):
  var=1
  for i in range(1,N+1):
    if i%2==0:
      var=0
    else:
      var=1
    for j in range(i):
      print(var,end=' ')
      var^=1
    print()

if __name__=="__main__":
  N=5
  printTriangle(N)