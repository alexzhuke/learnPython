__author__ = 'modoojunko'

import time

#this scripts is used to print logs for all scripts
contents = "Hello World!"


def print_factor(content, mark):
    print mark*(len(content) + 2*len(mark))
    print mark + content + mark
    print mark*(len(content) + 2*len(mark))


def time_factor():
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return local_time


def log_factory(content):
    current_time = time_factor()
    file_name = __file__.split("/")[-1]
    print "[" + current_time + " " + file_name + "]" + content


def print_head(content):
    print_factor(content, "#")


def print_sub_head(content):
    print_factor(content, "+")


def print_title(content):
    print_factor(content, "-")


def print_sub_title(content):
    print_factor(content, ":")



if __name__ == "__main__":
    print_head("head")
    print_sub_head("sub_head")
    print_title("title")
    print_sub_title("sub_title")
    log_factory("it is time to show the detail logs")
