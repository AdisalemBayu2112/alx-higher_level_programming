#!/usr/bin/python3
# Python program to print list
# by using loop

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
