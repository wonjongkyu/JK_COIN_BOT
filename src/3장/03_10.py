# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:55:31 2020

@author: jongkyu
"""

class Parent:
    def sing(self):
        print("sing a song")
        
class LuckyChild(Parent):
    def dance(self):
        print("shuffle dance")

luckyboy = LuckyChild()
luckyboy.sing()
luckyboy.dance()

