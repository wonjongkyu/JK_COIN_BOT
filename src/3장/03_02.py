# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:51:07 2020

@author: jongkyu
"""

""" 3.1 클래스 (1) """
class SuperMario:
    # 생성자
    def __init__(self):
        self.pos = 0
    # 함수 정의
    def forward(self):
        self.pos = self.pos + 20
        
# 객체 생성
mario = SuperMario()
# 함수 호출
mario.forward()
# 출
print(mario.pos)