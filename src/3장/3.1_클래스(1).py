# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" 3.1.2 클래스 정의 및 객체 생성 """
class MyClass:
    pass

obj = MyClass()
print(id(obj))


""" 3.1.4 붕어빵에 팥소 넣기 """
class 붕어빵틀:
    def 팥소넣기(self, 팥소):
        self.팥소 = 팥소
        
붕어빵1 = 붕어빵틀()
붕어빵틀.팥소넣기(붕어빵1, "초코맛팥소")
print(붕어빵1.팥소)
붕어빵2 = 붕어빵틀()
붕어빵틀.팥소넣기(붕어빵2, "딸맛팥소")
print(붕어빵2.팥소)

붕어빵1.팥소넣기("메론맛팥소")
붕어빵2.팥소넣기("커피맛팥소")
print(붕어빵1.팥소)
print(붕어빵2.팥소)


""" 3.1.5 초기화자 """
class 붕어빵틀:
    def __init__(self):
        self.팥소 = "초코맛팥소22"
        
붕어빵1 = 붕어빵틀()
print(붕어빵1.팥소)
print()



""" 연습문제 """
class Book:
    def __init__(self, 제목, 저자, 역자, 출판사, ISB10):
        self.제목 = 제목
        self.저자 = 저자
        self.역자 = 역자
        self.출판사 = 출판사
        self.ISB10 = ISB10
        
book = Book('테스트','김','철수','삼성출판사','13234')
print(book.제목)
