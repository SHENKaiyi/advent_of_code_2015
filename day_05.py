with open('input/day_05.txt', 'r') as file_object:
    lines = file_object.readlines()

nice_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
forbidden_substrings = ['ab', 'cd', 'pq', 'xy']

for line in lines:
    clean_string = line.strip()
    if not clean_string:
        continue
    vowel_count = 0
    for letter in clean_string:
        if letter in vowels:
            vowel_count = vowel_count + 1
    condition1 = (vowel_count >= 3)

    double_letter = False
    for i in range(len(clean_string) - 1):
        if clean_string[i] == clean_string[i + 1]:
            double_letter = True
            break
    condition2 = double_letter

    forbidden_letter = False
    for substring in forbidden_substrings:
        if substring in clean_string:
            forbidden_letter = True
            break
    condition3 = (not forbidden_letter)

    if condition1 and condition2 and condition3:
        nice_count = nice_count + 1
print(nice_count)

nice_count_part2 = 0

for line in lines:
    clean_string = line.strip()
    if not clean_string:
        continue

    repeated_pair = False  # 标记是否满足条件1
    for i in range(len(clean_string) - 1):
        current_pair = clean_string[i:i+2]
        if current_pair in clean_string[i+2:]:
            repeated_pair = True
            break
    condition1 = repeated_pair

    sandwich_letter = False
    for i in range(len(clean_string) - 2):
        if clean_string[i] == clean_string[i+2]:
            sandwich_letter = True
            break
    condition2 = sandwich_letter
    if condition1 and condition2:
        nice_count_part2 = nice_count_part2 + 1

print(nice_count_part2)