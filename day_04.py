import hashlib
with open('input/day_04.txt', 'r') as file_object:
    secret_key = file_object.read().strip()
for number in range(1, 10000000):
    combine_str = secret_key + str(number)
    md5_hash = hashlib.md5(combine_str.encode('utf-8')).hexdigest()
    # Usage of hashlib.md5() function from Doubao
    # Query prompt: "In Python, given a string, how to generate its MD5 hash and output it as a hexadecimal string?"
    if md5_hash[:5] == '00000':
        print(number)
        break

for number in range(1, 20000000):
    combine_str = secret_key + str(number)
    md5_hash = hashlib.md5(combine_str.encode('utf-8')).hexdigest()
    if md5_hash[:6] == '000000':
        print(number)
        break