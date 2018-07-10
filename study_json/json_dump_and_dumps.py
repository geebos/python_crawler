#-*- coding: utf-8 -*
__author__ = 'geebos'
import json


test = {
    "key1": "value1",
    "key2": [1,2,"value2"],
    "key3":
    {
        "key31": "value1",
        "key32": [1,2,"value2"],
        "key33": True,
        "key34": "测试",
    },
}

#没有设置 ensure_ascii为 False
with open('test.json', 'w', encoding='utf-8') as fp:
    json.dump(test, fp)
#设置了 ensure_ascii为 False
with open('test_no_ascii.json', 'w', encoding='utf-8') as fp:
    json.dump(test, fp, ensure_ascii=False)

#test.json的文件内容为：
#{... ... "key33": true, "key34": "\u6d4b\u8bd5"}}
#test_no_ascii.json的文件内容为：
#{... ... "key33": true, "key34": "测试"}}
#注意到 python中的 True转换成了 Javascript里的 true
#另外在打开文件的时候强烈建议用 encoding指定文件编码
#还需要注意文件的打开模式 w是写入，文件已存在的话就覆盖
#要追加写入的话记得用 a模式打开

test_string = json.dumps(test, ensure_ascii=False)
print(test_string)