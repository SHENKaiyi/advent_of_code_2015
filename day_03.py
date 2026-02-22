with open('input/day_03.txt', 'r') as file_object:
    directions = file_object.read().strip()
x = 0
y = 0
house = set()
house.add((x, y))
for move in directions:
    if move == '>':
        x = x + 1
    elif move == '<':
        x = x - 1
    elif move == '^':
        y = y + 1
    elif move == 'v':
        y = y - 1

    house.add((x, y))
house_count = len(house)
print(house_count)

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0

visited_houses = set()
visited_houses.add((0, 0))

for i, move in enumerate(directions):
    if i % 2 == 0:
        if move == '>':
            santa_x = santa_x + 1
        elif move == '<':
            santa_x = santa_x - 1
        elif move == '^':
            santa_y = santa_y + 1
        elif move == 'v':
            santa_y = santa_y - 1
        visited_houses.add((santa_x, santa_y))
    else:
        if move == '>':
            robo_x = robo_x + 1
        elif move == '<':
            robo_x = robo_x - 1
        elif move == '^':
            robo_y = robo_y + 1
        elif move == 'v':
            robo_y = robo_y - 1
        visited_houses.add((robo_x, robo_y))

total_houses = len(visited_houses)
print(total_houses)