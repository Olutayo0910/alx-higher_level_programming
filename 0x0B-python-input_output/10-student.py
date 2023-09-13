#!/usr/bin/python3
'''
file: 10-student.py
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Method that returns directory description with filter '''

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            re = {}
            for i in attrs:
                if i in self.__dict__:
                    re[i] = self.__dict__[i]
            return re
        return self.__dict__
