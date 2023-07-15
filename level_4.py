import requests
import re

num = 12345
num = str(16044/2)

while (True):
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={num}'
    text = requests.get(url).text
    print(text)
    pattern = r'and the next nothing is (\d+)'
    if num == None:
        break
    num = re.search(pattern, text).group(1)
    