#!/usr/bin/python3
"""Function that returns the list of available attributes"""

def lookup(obj):
    """ function that returns the list of available attributes
    and methods of an object"""
    return dir(obj)
