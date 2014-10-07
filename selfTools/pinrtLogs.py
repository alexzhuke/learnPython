__author__ = 'modoojunko'

#this scripts is used to print logs for all scripts
contents = "Hello World!"


def print_factor(content, mark):
    print mark*(len(content) + 2*len(mark))
    print mark + content + mark
    print mark*(len(content) + 2*len(mark))


def print_head(content):
    print_factor(content, "#")


def print_sub_head(content):
    print_factor(content, "+")


def print_title(content):
    print_factor(content, "-")


if __name__ == "__main__":
    print_head(contents)
    print_sub_head(contents)
    print_title(contents)
