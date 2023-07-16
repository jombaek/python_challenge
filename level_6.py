import zipfile
import re

f = zipfile.ZipFile(r'D:\Загрузки\channel.zip')
num = 90052
comments = []

while (True):
    file = f'{num}.txt'
    text = f.read(file).decode('utf-8')
    comments.append(f.getinfo(file).comment.decode('utf-8'))
    print(text)
    pattern = r'Next nothing is (\d+)'
    match = re.search(pattern, text)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))