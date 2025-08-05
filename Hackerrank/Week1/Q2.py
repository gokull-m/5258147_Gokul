def miniMaxSum(arr):
    # Write your code here
    n=sorted(arr)
    m=len(n)
    minvals=0
    maxvals=0
    for i in range(m-1):
      minvals+=n[i]
    for j in range(1,m):
      maxvals+=n[j]
      
    print(minvals,maxvals)