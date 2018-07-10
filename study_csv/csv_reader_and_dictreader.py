#-*- coding: utf-8 -*
__author__ = 'geebos'
import csv


#通过 reader读取文件内容 注意到之前我们设置了 delimiter为空格，这里也要继续设置为空格
with open('test_writer.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(row)


with open('test_dict_writer.csv', 'r', newline='', encoding='utf-8') as csvfile:
    dict_reader = csv.DictReader(csvfile, delimiter=' ')
    for row in dict_reader:
        print(row)