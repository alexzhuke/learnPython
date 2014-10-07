__author__ = 'modoojunko'
import os


path = "/Users/modoojunko/PycharmProjects"


def go_through_path(path):
    for root_dir, dirs, filenames in os.walk(path):
        for dir in dirs:
            print os.path.join(root_dir, dir)
        for filename in filenames:
            print os.path.join(root_dir, filename)