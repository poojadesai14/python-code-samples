import requests
import re
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
pd.array(r)
values = r.json()['data']

my_list = list()

for data in values.split(','):
    if data.startswith(' age='):
        my_list.append(data)

mid_list = list()

for x in my_list:
    mid_list.append(re.findall(r'[0-9]+', x))

final_list = list()

for i in mid_list:
    listToNum = int(''.join([str(ele) for ele in i]))
    final_list.append(listToNum)

count = 0
for num in final_list:
    if num >= 50:
        count += 1
print(count)
