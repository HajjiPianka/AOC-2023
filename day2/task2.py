file = open('./day2/data.txt','r')
f = file.readlines()
file.close()
"""
def is_valid(number: int, color: str) -> bool:
    '''checks if number of specific cubes is allowed'''
    match color:
        case 'red':
            if number > red:
                return False
            return True
        case 'green':
            if number > green:
                return False
            return True
        case 'blue':
            if number > blue:
                return False
            return True
"""
def draws(draws: list[str]) -> bool:
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            cube = cube.strip()
            cube = cube.split(' ')
            quantity = int(cube[0]) #get number of cubes
            color = cube[1] #get color of cubes
            # if not is_valid(quantity, color):
            #     return False
    # return True

sum = 0
for i in f:
    i = i.strip().replace(':',';')[5:].split(';')
    id = i[0]
    i = i[1:] #remove id from data
    if draws(i):
        sum += int(id)

file = open('./day2/result2.txt','w')
file.write(f'Answer: {sum}')
file.close()