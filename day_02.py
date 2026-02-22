with open('input/day_02.txt', 'r') as file_object:
    lines = file_object.readlines()
total_paper = 0
total_ribbon = 0
for line in lines:
    size = line.strip()
    if not size:
        continue

    size_list = size.split('x')
    l = int(size_list[0])
    w = int(size_list[1])
    h = int(size_list[2])
    area1 = l * w
    area2 = w * h
    area3 = h * l
    surface_area = 2 * area1 + 2 * area2 + 2 * area3
    min_area = min(area1, area2, area3)
    total_paper = total_paper + surface_area + min_area

    sides = [l, w, h]
    sorted_sides = sorted(sides)
    min_perimeter = 2 * (sorted_sides[0] + sorted_sides[1])
    volume = l * w * h
    single_ribbon = min_perimeter + volume
    total_ribbon = total_ribbon + single_ribbon
print(total_paper)
print(total_ribbon)
