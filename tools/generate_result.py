# coding=utf-8
'''
Created on 2020-04-24, 15:14
@author: Qiuyu Cai
'''
import json

result = json.load(open("../data/result.json"))
sentences = json.load(open("../data/validate_data.json", encoding="utf-8"))
index = 0
count = 0
for k, v in sentences.items():
    if len(list(v)) == len(result[index]):
        count += 1
    print(len(list(v)), end="----")
    print(k, end="----")
    print(len(result[index]))

    index += 1
print(count)