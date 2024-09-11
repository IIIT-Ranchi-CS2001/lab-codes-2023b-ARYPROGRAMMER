num = int(input("ENTER num : "))
s=0
while (num>1):
    s+=num%10
    num//=10
print(f"Sum : {s}")