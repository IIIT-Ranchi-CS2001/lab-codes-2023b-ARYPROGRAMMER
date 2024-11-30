n = int(input("ENTER NUMBER : "))
l = int(input("ENTER LIMIT : "))
print(f"MULTIPLICATION TABLE OF {n}")
for i in range(1,l+1):
    print(f"{n}x{i} = {n*i}")