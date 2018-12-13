import collections

def get_input():
    with open('input.txt', 'r') as f:
        data = [[a for a in row] for row in f.read().split('\n')]
    
    cars = []

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '<':
                cars.append([y, x, (0,-1), 'L'])
                data[y][x] = '-'
            elif data[y][x] == '>':
                cars.append([y, x, (0,1), 'L'])
                data[y][x] = '-'
            elif data[y][x] == '^':
                cars.append([y, x, (-1,0), 'L'])
                data[y][x] = '|'
            elif data[y][x] == 'v':
                cars.append([y, x, (1,0), 'L'])
                data[y][x] = '|'
    return data, cars

def move_car(car, roads):
    car[0], car[1] = car[0]+car[2][0], car[1]+car[2][1]
    road = roads[car[0]][car[1]]
    if road in ('/', '\\', '+'):
        car = turn_car(car, road)
    return car

def turn_car(car, road):
    turn_order = {
        'L': 'S',
        'S': 'R',
        'R': 'L'
    }

    if road == '+':
        turn = car[3]
        car[3] = turn_order[car[3]]
    elif (road == '/' and car[2][0] != 0) or (road == '\\' and car[2][0] == 0):
        turn = 'R'
    else:
        turn = 'L'

    if turn == 'S':
        pass
    elif (turn == 'R' and car[2][0] == 0) or (turn == 'L' and car[2][1] == 0):
        car[2] = (car[2][1], car[2][0])
    else:
        car[2] = (-car[2][1], -car[2][0])
    return car

def check_collisions(cars):
    positions = [(car[0], car[1]) for car in cars]
    collisions = [position for position, count in collections.Counter(positions).items() if count > 1]
    collision_indices = []
    for i in range(len(cars)):
        if (cars[i][0], cars[i][1]) in collisions:
            collision_indices.append(i)
    cars = [car for car in cars if (car[0], car[1]) not in collisions]
    return cars, collision_indices

roads, cars = get_input()

while True:
    cars.sort()
    breaker = False
    i = 0
    while True:
        cars[i] = move_car(cars[i], roads)
        cars, collision_indices = check_collisions(cars)

        if collision_indices:
            if min(collision_indices) < i:
                i -= 1
            else:
                pass
        else:
            i += 1
        if len(cars) == 1:
            breaker = True
        if i >= len(cars):
            break
    if breaker:
        break
print(cars)


