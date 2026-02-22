with open('input/day_01.txt', 'r') as file_object:
    input_text = file_object.read().strip()
floor = 0
for bracket in input_text:
    if bracket == '(':
        floor = floor + 1
    elif bracket == ')':
        floor = floor - 1
print(floor)