n = int(input("ENTER NUMBER OF TERMS OF FIBONACCI : "))

a=0
b=1
print(a,end=",")
for i in range(1,n):
    print(b,end=",")
    c=a+b
    a=b
    b=c