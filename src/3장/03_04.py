# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:07:35 2020

@author: jongkyu
"""

class SuperMario:
    def __init__(self):
        self.pos = 0
        
    def forward(self):
        self.pos = self.pos + 20
        
mario_p1 = SuperMario()
mario_p2 = SuperMario()
mario_p1.forward()
mario_p2.forward()

print()

a = 3
print(type(a))
print(a.bit_length())

b = "python"
print(type(b))
print(b.upper())


