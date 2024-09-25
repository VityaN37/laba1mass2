n=2
a=[[0]*n for _ in range(n)]
k = int(input())
d=[[2,2],
   [2,2]]
for i in range(n): #a*f
    for j in range(n):
       a[i][j]=d[i][j]*k

for i in a:
    print(i)