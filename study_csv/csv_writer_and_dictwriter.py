#-*- coding: utf-8 -*
__author__ = 'geebos'
import csv


#通过 writer类写入数据
#待写入的数据 注意到两个列表的元素个数不一样
test_writer_data_1 = ['Tom', 'Cody', 'Zack']
test_writer_data_2 = ['Mike', 'Bill']

#创建并打开文件
with open('test_writer.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #获得 writer对象 delimiter是分隔符 默认为 ","
    writer = csv.writer(csvfile, delimiter=' ')
    #调用 writer的 writerow方法将 test_writer_data写入 test_writer.csv文件
    #writer.writerow(test_writer_data_1)
    #writer.writerow(test_writer_data_2)
    writer.writerows([test_writer_data_1, test_writer_data_2])


#通过 DictWriter类写入数据
#待写入的数据 注意到待写入的数据类型为 dict 且第二个字典没有 lastname
test_dict_writer_data_1 = {'firstname': 'Tom', 'lastname': 'Loya'}
test_dict_writer_data_2 = {'firstname': 'Tom'}

#创建并打开文件
with open('test_dict_writer.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #设置表头
    fieldnames=['firstname', 'lastname']
    # 获得 DictWriter对象 delimiter是分隔符 默认为 "," 表头为 'firstname' 'lastname'
    dict_writer = csv.DictWriter(csvfile, delimiter=' ', fieldnames=fieldnames, strict=True)
    #第一次写入数据先写入表头
    dict_writer.writeheader()
    #调用 DictWriter的 writerow方法将 test_dict_writer_data写入 test_dict_writer.csv文件
    #dict_writer.writerow(test_dict_writer_data_1)
    #dict_writer.writerow(test_dict_writer_data_2)
    dict_writer.writerows([test_dict_writer_data_1, test_dict_writer_data_2])



