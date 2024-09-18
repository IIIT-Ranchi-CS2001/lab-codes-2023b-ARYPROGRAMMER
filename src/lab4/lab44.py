singer = eval(input("ENTER SET 1 : "))
dancer = eval(input("ENTER SET 2 : "))

all = singer | dancer
allr = singer & dancer

dns = dancer-singer
snd = singer-dancer
dors = (dancer-singer)|(singer-dancer)
print("ALL ARTIST",all)
print("ALL ROUNDERS",allr)
print("DANCER BUT NOT SINGER",dns)
print("SINGER BUT NOT DANCER",snd)
print("ALL ARTIST",all)
print("DANCER BUT NOT SINGER OR SINGER BUT NOT DANCER",dors)
