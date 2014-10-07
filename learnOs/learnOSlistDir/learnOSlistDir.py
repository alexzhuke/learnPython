__author__ = 'modoojunko'
import os

path = "/Users/modoojunko/zhuke"


def listdir(dir):
    file_list = os.listdir(dir)
    for line in file_list:
        filepath = os.path.join(dir, line)
        if os.path.isdir(filepath):
            print filepath
            listdir(filepath)
        elif os.path.isfile(filepath):
            print filepath
listdir(path)