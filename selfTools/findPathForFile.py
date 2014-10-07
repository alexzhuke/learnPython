__author__ = 'modoojunko'

import os


def get_current_path():
    current_path = os.getcwd()
    return current_path


def get_list_from_path(path):
    #path_list = os.walk(path)
    for path_list in os.walk(path):
        print path_list


a = get_current_path()


b = get_list_from_path("/Users/modoojunko/PycharmProjects/learnPython")

print a
print b