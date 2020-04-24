# coding=utf-8
'''
Created on 2020-04-24, 12:14
@author: Qiuyu Cai
'''
import json
import os
from tqdm import tqdm


map_dict = {"试验要素": ["B-TEST", "I-TEST"],
            "性能指标": ["B-RANK", "I-RANK"],
            "系统组成": ["B-SYS", "I-SYS"],
            "任务场景": ["B-TASK", "I-TASK"]}

#  prepare train data
base_path = "../data/train"
file_list = sorted(os.listdir(base_path))
print(file_list[199])
result = []
for fi in tqdm(file_list):
    pa = os.path.join(base_path, fi)
    json_re = json.load(open(pa,  encoding="gbk"))
    text_ele = list(json_re["originalText"].strip())
    elements = json_re["entities"]
    tag_ele = ["O" for i in range(len(text_ele))]
    for ele in elements:
        label_name = map_dict[ele["label_type"]]
        tag_ele[ele["start_pos"] -1] = label_name[0]
        for i in range(ele["start_pos"], ele["end_pos"]):
            tag_ele[i] = label_name[1]
    result.append((text_ele, tag_ele))
print(len(result))

len_be = []
with open("../data/msra_train_bio", "w", encoding="utf-8") as fw:
    for re in result:
        ind = 0
        for word, tag in zip(re[0], re[1]):
            if word == " ":
                continue
            fw.write(word + "\t" + tag)
            fw.write("\n")
            ind += 1
        len_be.append(ind)
        fw.write("\n")
print(len_be)

# load test data
result = []
len_test = []
test_data = json.load(open("../data/validate_data.json", encoding="utf-8"))
for k, v in test_data.items():
    text = list(v.strip().replace(" ", ""))
    tag = ["O" for i in range(len(text))]
    result.append((text, tag))
    len_test.append(len(text))

with open("../data/msra_test_bio", "w", encoding="utf-8") as fw:
    for re in result:
        for word, tag in zip(re[0], re[1]):
            if word == " ":
                continue
            fw.write(word + "\t" + tag)
            fw.write("\n")
        fw.write("\n")
