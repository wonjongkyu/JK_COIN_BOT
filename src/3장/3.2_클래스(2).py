# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:51:16 2020

@author: jongkyu
"""

""" 3.2.2. 클래스 속성 참조 순서 """
class B:
    pass


inst1 = B()
inst2 = B()
inst1.data = 3
inst2.num = 4


print(inst1.data)
print(inst1.num)