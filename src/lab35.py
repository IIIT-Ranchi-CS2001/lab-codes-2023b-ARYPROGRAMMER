s = input("enter string : ")
ss = None
for i in s:
    if i.isalpha or i.isdigit:
        ss = True
    else:
        ss=False
print(ss)