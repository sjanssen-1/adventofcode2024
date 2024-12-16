import sys

def findStart(map: list[list[str]]):
    xl = len(map[0])
    yl = len(map)
    for y in range(yl):
        for x in range(xl):
            if map[y][x] == '^':
                return x, y

def changeDirection(direction: str):
    match direction:
        case "up":
            return "right"
        case "right":
            return "down"
        case "down":
            return "left"
        case "left":
            return "up"
        
def hasLoop(map):
    start = findStart(map)
    x = start[0]
    y = start[1]
    current_direction = "up"
    locations = set()

    while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
        pos = map[y][x]

        if pos == "#":
            if current_direction == "up":
                y+=1
            elif current_direction == "right":
                x-=1
            elif current_direction == "down":
                y-=1
            else: # left
                x+=1
            current_direction = changeDirection(current_direction)
            continue
        
        if (x,y,current_direction) in locations:
            return True

        locations.add((x,y,current_direction))

        if current_direction == "up":
            y-=1
        elif current_direction == "right":
            x+=1
        elif current_direction == "down":
            y+=1
        else: # left
            x-=1
    return False


# main
if len(sys.argv) > 1 and sys.argv[1] == '-real':
    file = open("day6.in", "r")
else:
    file = open("day6_sample.in", "r")


map = list(map(list, file.read().splitlines()))

start = findStart(map)

x = start[0]
y = start[1]
current_direction = "up"
unique_locations = set()

while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
    pos = map[y][x]

    if pos == "#":
        if current_direction == "up":
            y+=1
        elif current_direction == "right":
            x-=1
        elif current_direction == "down":
            y-=1
        else: # left
            x+=1
        current_direction = changeDirection(current_direction)
        continue

    unique_locations.add((x,y))

    if current_direction == "up":
        y-=1
    elif current_direction == "right":
        x+=1
    elif current_direction == "down":
        y+=1
    else: # left
        x-=1

loops = 0
for unique_location in unique_locations:
    if unique_location == start:
        continue

    newx = int(unique_location[0])
    newy = int(unique_location[1])
    map[newy][newx] = '#'
    if hasLoop(map):
        loops+=1
    map[newy][newx] = '.'



print("loops: " + str(loops))