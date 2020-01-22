# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:31:54 2020

@author: jongkyu
"""

class MyClass:
    def method(self):
        print("method")
    def add(self, a, b):
        return a + b

obj = MyClass()
obj.method()
print(obj.add(1,3))

