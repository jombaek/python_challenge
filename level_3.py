import re

pattern = r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'

with open('level_3.txt', 'r') as fin:
    text = fin.read()
    print("".join(re.findall(pattern, text)))