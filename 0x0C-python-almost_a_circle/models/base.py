#!/usr/bin/python3
class Base:
    """Base of all classes
    Private class attribute __nb_object
    is the number of instantiated Bases"""
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        self.id = id
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            