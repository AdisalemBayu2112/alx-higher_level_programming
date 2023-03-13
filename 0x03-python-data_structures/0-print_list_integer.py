#!/usr/bin/python3
# Python program to print list
# without using loop

def print_list_integer(my_list=[]): 
    my_list = [1, 2, 3, 4, 5]
    print(*my_list, sep = "\n")
