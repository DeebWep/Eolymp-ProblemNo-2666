a = int(input())
c = a-1
for i in range(a):
    k = ""
    for j in range(a):
        if i == 0 and j!=a-1:
            k+='2'
        if (i!=0 and i!=a-1) and j<c:
            k+='2'
        if (i!=0 and i!=a-1) and j>c:
            k+='1'
        if j==c:
            k+='0'
            c=c-1
        if i ==a-1 and j!=0:
            k+='1'
    print(k)
