import random
a = []
'''Формируется матрица F следующим образом: Скопировать в нее матрицу А и если 
количество нулей в нечетных столбцах в области 4 больше, чем сумма чисел в нечетных 
строках в области 1, то поменять симметрично области 1 и 2 местами, иначе 2 и 3 
поменять местами несимметрично. При этом матрица А не меняется. После чего 
вычисляется выражение: (К*(A*F)– K*AT . Выводятся по мере формирования А, F и все 
матричные операции последовательно.
print("enter n number 3 to 100")'''
n = int(input())
print("enter k number -... to 100")
l = int(input())
print("enter number 1 or 2 ")
print("1.filling with file")
print("2.filling random")
choice = int(input())

# инициализация матрицы а
if choice==1:
    file = open('massA.txt', 'r')
    for i in range(n):
        st = file.readline()
        a.append([int(x) for x in st.split()])

    print("A")
    for i in a:
        print(i)

elif choice==2:
    a=[[random.randint(-10,10) for _ in range(n)] for _ in range(n)]
    print("A")
    for i in a:
        print(i)
else:
    print("incorrect input")



print("F")
f = [[0]*n for _ in range(n)]
for i in f:
    print(i)

for i in range(n):      #копирую a в f
    for j in range(n):
        f[i][j] = a[i][j]
print("F")
for i in f:
    print(i)


sum0=0
sumnum=0
d=[]
k=[]
#for i in range(n):
    #for j in range(n):
        #if j % 2 != 0 :
            #if i > j and i+j>size-1:
                #if f[i][j] == 0:
                    #sum0+=1
        #elif j % 2 != 0 or j == 0:
            #if i > j and i + j < size-1:
               #sumnum+=f[i][j]

for i in range(n-1,n//2,-1): # fourth area
    for j in range(n-i,n//2):
        if f[i][j]==0:
            #print(f'{f[i][j]}*')
            #print(f'{i},{j}')
            sum0 +=1

for i in range(n//2,n): # почему i считается с 4 , а j с 3
    for j in range(n//2,i):
       if f[i][j] == 0:
           #print(f'{f[i][j]}.')
           #print(f'{i},{j}')
           sum0 += 1


for i in range(n//2): # first area
    for j in range(i):
        sumnum+=f[i][j]
for i in range(n//2,n):
    for j in range(n-(i+1)):
        sumnum+=f[i][j]
print(sumnum)
print(sum0)
t=0
y=0

if sum0 > sumnum :
    for i in range(n): #2
        for j in range(n):
            if i<j and i+j < n-1:
                d.append(f[i][j])
    for j in range(n): #1
        for i in range(n-1,-1,-1):
            if i > j and i + j < n - 1:
                 k.append(f[i][j])
    for i in range(n):
        for j in range(n):
            if i < j and i + j < n - 1:
                f[i][j]=k[t]
                t+=1
    for j in range(n) :
        for i in range(n-1,-1,-1):
            if i > j and i + j < n - 1 :
                f[i][j]=d[y]
                y+=1
    print("F1 then sum0 > sumnum")
    for i in f:
        print(i)

else:
    for i in range(n): #2
        for j in range(n):
            if i<j and i+j < n-1:
                d.append(f[i][j])
    for j in range(n-1,-1,-1): #3
        for i in range(n):
             if i < j and i + j >n - 1:
                 k.append(f[i][j])
    for i in range(n):
        for j in range(n-1,-1,-1):
            if i < j and i + j < n - 1:
                f[i][j]=k[t]
                t+=1
    for j in range(n-1,-1,-1):
        for i in range(n-1,-1,-1):
            if i < j and i + j > n - 1:
                f[i][j]=d[y]
                y+=1

    print("F2 then sum0 < sumnum")
    for i in f:
        print(i)

p=0
#print("D")
#print(d)
#print("K")
#print(k)
c = [[0]*n for _ in range(n)]
for i in range(n): #a*f
    for j in range(n):
        s=0
        for p in range(n):
            s+=a[i][p]*f[p][j]
        c[i][j]=s
print("c")
for i in c:
    print(i)

x= [[0]*n for _ in range(n)]

for i in range(n):            #k*c
    for j in range(n):
        c[i][j]*=l

print("c")
for i in c:
    print(i)

at = [[0]*n for _ in range(n)]
for i in range(n): #at
    for j in range(n):
        at[i][j]=a[j][i]
print("at")
for i in at:
    print(i)

atk=[[0]*n for _ in range(n)]
for i in range(n): #at*k
    for j in range(n):
        atk[i][j]=at[i][j]*l
print("atk")
for i in atk:
    print(i)

m=[[0]*n for _ in range(n)]
for i in range(n): #c-atk
    for j in range(n):
        m[i][j]=c[i][j]-atk[i][j]
print("result")
for i in m:
    print(i)



