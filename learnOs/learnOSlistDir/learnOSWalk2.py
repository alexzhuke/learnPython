__author__ = 'modoojunko'
import os


path = "/Users/modoojunko/PycharmProjects"


def go_through_path(path):
    for root_dir, dirs, filenames in os.walk(path):
        for dir in dirs:
            print os.path.join(root_dir, dir)
        for filename in filenames:
            print os.path.join(root_dir, filename)


def find_file(arg,dirname,files):

    for file in files:

        file_path = os.path.join(dirname, file)

        if os.path.isfile(file_path):

            print "find file:%s" %file_path


os.path.walk(path,find_file,())