file = open('./day1/data.txt','r')
f = file.readlines()
file.close()
sum = 0
def digit(string: str, reverse: bool = False):
    '''Returns first digit of a string, parsed with second argument returns last digit'''
    string = string.strip()
    ###part 2
    # insert digits into detected numbers
    strings =  ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = ['o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']
    for i in range(9):
        string = string.replace(strings[i],numbers[i])
    ###
    if reverse:
        string = string[::-1]
    for i in string:
        try:
            x = int(i)
            return x
        except:
            continue
def merge_ints(num1: int, num2: int):
    return int(str(num1) + str(num2))

for i in f:
    i = i.strip()
    num1 = digit(i)
    num2 = digit(i,True)
    number = merge_ints(num1,num2)
    sum += number
file = open('./day1/result2.txt','w')
file.write(f'Answer: {sum}')
file.close()