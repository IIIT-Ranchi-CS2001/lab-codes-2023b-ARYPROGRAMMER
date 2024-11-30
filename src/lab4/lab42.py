l = eval(input("ENTER LIST OF INTEGERS : "))
l.sort()
mean = sum(l)/len(l)

if len(l)%2!=0:
    mid = int((len(l)+1)/2)
    median = l[mid]
else:
    m1 = mid = int((len(l))/2)
    m2=m1+1
    k1 = l[m1]
    k2=l[m2]
    median = (k1+k2)/2
key=l[0]
key_count=l.count(key)

for i in l:
    test = l.count(i)

    if (test>key_count):
        key_count=test
        key=i
mode=key
print(f"MEAN IS {mean}, MEDIAN IS {median}, MODE IS {mode}")