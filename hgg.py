n=6
a=[]
file = open('massA.txt', 'r')
for i in range(n):
    st = file.readline()
    a.append([int(x) for x in st.split()])

print("A")
for i in a:
    print(i)

for i in range(n):
    for j in range(i):
        print(i,j)