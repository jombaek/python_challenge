my_dict = dict()

with open('level_2.txt', 'r') as fin:
    for line in fin:
        for c in line:
            if c not in my_dict:
                my_dict[c] = 1
            else:
                my_dict[c] += 1

min_count = min(my_dict.values())
res = ""

for key, value in my_dict.items():
    if value == min_count:
        res += key

print(res)