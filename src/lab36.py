s = input("enter string : ")
c = input("enter character to find : ")
co=0
for i in s:
    if i==c:
        co+=1

print(f"{c} occurred {co} times in {s}")