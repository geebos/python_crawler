#-*- coding: utf-8 -*
__author__ = 'geebos'
import json


#json格式的字符串
test_string = '{"key1": "value1", "key2": [1, 2, "value2"], "key3": {"key31": "value1", "key32": [1, 2, "value2"], "key33": true, "key34": "测试"}}'

#从之前保存的 test_no_ascii.json中读取 注意模式为 r
with open('test_no_ascii.json', 'r', encoding='utf-8') as fp:
    json_obj_from_file = json.load(fp)

json_obj_from_web = json.loads(test_string)

#打印两个返回结果的类型
print(type(json_obj_from_file))
print(type(json_obj_from_web))
#打印两个返回结果的内容
print(json_obj_from_file)
print(json_obj_from_web)