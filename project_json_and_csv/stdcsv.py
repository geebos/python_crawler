#-*- coding: utf-8 -*
__author__ = 'geebos'
import csv
import os


class writer:
    def __init__(self, filepath, *args, **kwds):
        if filepath == None:
            raise ValueError("filepath can't be None")
        self.keys, self.csvfile = self._get_file_obj(filepath)
        self.dict_writer = None
        self.args = args
        self.kwds = kwds

        #print(self.keys, args, kwds)

    def __del__(self):
        self.csvfile.close()
        print('the file is closed.')


    def _get_file_obj(self, filepath):
        if self._file_exist(filepath):
            with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                keys = csvfile.readline().strip().split(',')
            csvfile = open(filepath, 'a', newline='', encoding='utf-8')
            return keys, csvfile
        else:
            return None, open(filepath, 'w', newline='', encoding='utf-8')


    def _file_exist(self, filepath):
        if os.path.isfile(filepath):
            return True
        elif os.path.isfile(os.getcwd()+filepath):
            return True
        else:
            return False

    def _row_keys_match(self, row):
        row_keys = list(row.keys())

        if len(row_keys) != len(self.keys):
            return  False
        else:
            for key in self.keys:
                if key not in row_keys:
                    return False
            for row_key in row_keys:
                if row_key not in self.keys:
                    return False
        return True

    def writerow(self, row):
        if not isinstance(row, dict):
            raise TypeError('row must be a dict')
        if self.dict_writer is None and self.keys is None:
            self.keys = list(row.keys())
            self.dict_writer = csv.DictWriter(self.csvfile, fieldnames=self.keys, *self.args, **self.kwds)
            self.dict_writer.writeheader()
            self.dict_writer.writerow(row)
        elif self.dict_writer is None and self.keys != None:
            if not self._row_keys_match(row):
                raise KeyError("dict kyes not match the writer object's keys")
            self.dict_writer = csv.DictWriter(self.csvfile, fieldnames=self.keys, *self.args, **self.kwds)
            self.dict_writer.writerow(row)
        else:
            if not self._row_keys_match(row):
                raise KeyError("dict kyes not match the writer object's keys")
            self.dict_writer.writerow(row)

class reader:
    def __init__(self, filepath, *args, **kwds):
        keys, csvfile = self._get_file_obj(filepath)
        self.reader = csv.DictReader(csvfile, keys)

    def _get_file_obj(self, filepath):
        if self._file_exist(filepath):
            with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                keys = csvfile.readline().strip().split(',')
            csvfile = open(filepath, 'a', newline='', encoding='utf-8')
            return keys, csvfile
        else:
            raise ValueError('file not exist.')

    def _file_exist(self, filepath):
        if os.path.isfile(filepath):
            return True
        elif os.path.isfile(os.getcwd()+filepath):
            return True
        else:
            return False

    def readerow(self):
        for row in self.reader:
            d={}
            for t in row:
                d[t[0]] = t[2]
            yield d