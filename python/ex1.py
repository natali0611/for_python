#!/usr/bin//env python

def deco(func):
    print("decoratore start")
    return func

@deco
def my_func(x):
    return x * 2


if _name_=="_main_":
    print(my_func(2))
