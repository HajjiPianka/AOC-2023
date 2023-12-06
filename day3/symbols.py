file = open('./day3/data.txt','r')
f = file.readlines()
file.close()
a = []
for i in f:
    for j in i.strip():
        try:
            int(j)
        except:
            if j != '.':
                a.append(j)
print(set(a))