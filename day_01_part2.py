with open('input/day_01.txt', 'r') as file_object:
    input_text = file_object.read().strip()
found = False
floor = 0
for position, bracket in enumerate(input_text, start=1):
    if found:
        continue
    if bracket == '(':
        floor = floor + 1
    elif bracket == ')':
        floor = floor - 1
    if floor == -1:
        print(position)
        found = True