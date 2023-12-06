chars = ['%', '-', '&', '=', '*', '/', '+', '#', '@', '$']

file = open("./day3/data.txt",'r')
f = file.readlines()
file.close()
lin1 = ''
lin2 = ''
lin3 = f[0].strip()
sum = 0
for a in range(0,len(f)+1):
    lin1 = lin2
    lin2 = lin3
    try:
        lin3 = f[a+1].strip()
    except:
        lin3 = ''
    indexy = []
    number = ''
    for i in range(len(lin2)):
        znak = lin2[i]
        try:
            int(znak)
            number += znak
            indexy.append(i)
        except:
            if number == '':
                continue
            else:
                symbol = False
                substr1 = lin1[indexy[0]:indexy[-1]+1]
                substr2 = lin2[indexy[0]:indexy[-1]+1]
                try:
                    substr3 = lin3[indexy[0]:indexy[-1]+1]
                except:
                    pass
                rest = ''
                try:
                    rest += lin1[indexy[0]-1]
                except:
                    pass
                try:
                    rest += lin1[indexy[-1]+1]
                except:
                    pass
                try:
                    rest += lin2[indexy[0]-1]
                except:
                    pass
                try:
                    rest += lin2[indexy[-1]+1]
                except:
                    pass
                try:
                    rest += lin3[indexy[0]-1]
                except:
                    pass
                try:
                    rest += lin3[indexy[-1]+1]
                except:
                    pass
                
                rest += substr1 + substr2
                try:
                    rest += substr3
                except:
                    pass

                for char in chars:
                    if char in rest:
                        symbol = True
                if symbol:
                    sum += int(number)
            number = ''
            indexy.clear()
            substr1 = ''
            substr2 = ''
            substr3 = ''
            rest = ''
file = open('./day3/result1.txt','w')
file.write(f'Answer: {sum}')
file.close()