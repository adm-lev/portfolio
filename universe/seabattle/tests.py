

from django.test import TestCase


def add_num(path):
    import os
    with open(path) as file:
        with open(path + '11', 'a') as file2:
            for num, line in enumerate(file):
                file2.write(str(num + 1) + ' ' + line)
    os.rename(path + '11', path)



add_num('sample.txt')

