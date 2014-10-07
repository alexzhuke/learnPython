__author__ = 'modoojunko'
import os


path = "/Users/modoojunko/PycharmProjects"


def go_through_path(path):
    for root_dir, dirs, filenames in os.walk(path):
        for dir in dirs:
            full_path = os.path.join(root_dir, dir)
            print full_path
        for filename in filenames:
            full_path = os.path.join(root_dir, filename)
            print full_path