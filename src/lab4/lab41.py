s = input("ENTER A STRING : ")
l = s.split()
c=0
for i in l:
    if i == i[::-1] and i.isnumeric == False:
        c+=1
print(f"{c} palindromes")