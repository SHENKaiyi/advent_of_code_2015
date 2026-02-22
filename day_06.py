grid = []
for _ in range(1000):
    row = [False] * 1000
    grid.append(row)

with open('input/day_06.txt', 'r') as file_object:
    instructions = file_object.readlines()

for line in instructions:
    cmd = line.strip()
    if not cmd:
        continue

    if 'turn on' in cmd:
        operation = 'on'
        coord_part = cmd.replace('turn on ', '')
    elif 'turn off' in cmd:
        operation = 'off'
        coord_part = cmd.replace('turn off ', '')
    elif 'toggle' in cmd:
        operation = 'toggle'
        coord_part = cmd.replace('toggle ', '')
    else:
        continue

    coord_pairs = coord_part.split(' through ')
    x1_str, y1_str = coord_pairs[0].split(',')
    x1 = int(x1_str)
    y1 = int(y1_str)
    x2_str, y2_str = coord_pairs[1].split(',')
    x2 = int(x2_str)
    y2 = int(y2_str)

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if operation == 'on':
                grid[x][y] = True
            elif operation == 'off':
                grid[x][y] = False
            elif operation == 'toggle':
                grid[x][y] = not grid[x][y]

lit_count = 0
for x in range(1000):
    for y in range(1000):
        if grid[x][y] is True:
            lit_count = lit_count + 1
print(lit_count)

grid_brightness = []
for _ in range(1000):
    row = [0] * 1000
    grid_brightness.append(row)

for line in instructions:
    cmd = line.strip()
    if not cmd:
        continue

    if 'turn on' in cmd:
        operation = 'on'
        coord_part = cmd.replace('turn on ', '')
    elif 'turn off' in cmd:
        operation = 'off'
        coord_part = cmd.replace('turn off ', '')
    elif 'toggle' in cmd:
        operation = 'toggle'
        coord_part = cmd.replace('toggle ', '')
    else:
        continue

    coord_pairs = coord_part.split(' through ')
    x1, y1 = map(int, coord_pairs[0].split(','))
    x2, y2 = map(int, coord_pairs[1].split(','))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if operation == 'on':
                grid_brightness[x][y] += 1
            elif operation == 'off':
                grid_brightness[x][y] = max(0, grid_brightness[x][y] - 1)
            elif operation == 'toggle':
                grid_brightness[x][y] += 2

total_brightness = 0
for x in range(1000):
    for y in range(1000):
        total_brightness += grid_brightness[x][y]
print(f"\n===== Part2 结果 =====")
print(f"所有灯的总亮度: {total_brightness}")