import requests
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
res = requests.get(url)
data = pickle.loads(res.content)

for line in data:
    print("".join([k * v for k, v in line]))