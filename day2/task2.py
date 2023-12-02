file = open('./day2/data.txt','r')
f = file.readlines()
file.close()

def min_color(draws: list[str]) -> bool:
    #data 
    red, green, blue = 0, 0, 0
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            cube = cube.strip()
            cube = cube.split(' ')
            quantity = int(cube[0]) #get number of cubes
            color = cube[1] #get color of cubes
            match color:
                case 'red':
                    red = red if red > quantity else quantity
                case 'green':
                    green = green if green > quantity else quantity
                case 'blue':
                    blue = blue if blue > quantity else quantity
    return [red, green, blue]

sum = 0
for i in f:
    i = i.strip().replace(':',';')[5:].split(';')
    id = i[0]
    i = i[1:] #remove id from data
    min_values = min_color(i)
    curr = min_values[0] * min_values[1] * min_values[2]
    sum += curr
    curr = 0

file = open('./day2/result2.txt','w')
file.write(f'Answer: {sum}')
file.close()