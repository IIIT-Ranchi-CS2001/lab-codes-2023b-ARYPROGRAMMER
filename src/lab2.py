# s1 = "Maha Bharat"
# s=""
# m=s1.split(" ")
# for i in s1:
#     if i=="M":
#         s+="m"
#         continue
#     if i=="B":
#         s+="b"
#         continue
#     s+=i.upper()   

# print("1 .",s)
# print("2 .",m[1])
# print("3 .",m[1]*3)
# print("4 .","Mera"+" "+m[1])
# print("5 .","Mera"+" "+m[1]+" Mahan")

# s = "Ba Ba Black Sheep"
# print("1 .",len(s))
# print("2 .",s.find("e"))
# print("3 .",s.count("a"))
# s=s.replace("B","T",2)
# print("4 .",s)

# s=input("ENTER STRING : ")
# if (s==s[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")

# name = input("enter name : ")
# roll = input("enter roll : ")
# marks = int(input("enter marks (out of 100) : "))
# if marks>= 90:
#     gp=10
#     remarks="OUTSTANDING"
# if (90 > marks >= 80):
#     gp=9
#     remarks = "VERY GOOD"

# if (80 > marks >= 70):
#     gp=8
#     remarks="GOOD"

# if (70 > marks >= 60):
#     gp=7
#     remarks="AVERAGE"

# if (60 > marks >= 50):
#     gp=6
#     remarks="PASS"

# if (marks < 50):
#     gp=0
#     remarks="FAIL"

# print("___________________")
# print("Name :",name)
# print("Roll Number :",roll)
# print("Marks :",marks)
# print("Grade Point :",gp)
# print("Remark :",remarks)

import cmath
a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))
d= b**2 - 4*a*c

if (d==0):
    R1 = -b/(2*a)
    R2=R1
if (d>0):
    R1 = (-b + d**0.5)/2*a
    R2 = (-b - d**0.5)/2*a

if (d<0):
    R1 = -b/(2*a)
    R2 = (cmath.sqrt(d))/2*a

print(f"Root 1 : {R1}  and Root 2 : {R2}")