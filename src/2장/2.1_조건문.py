# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" if 문 테스트 """
bitcoin = 8400000
if bitcoin > 10000000:
    print('bitcoin 매수')
    

""" if elseif else문 테스트 """
ripple = 500
if ripple > 600:
    print('ripple 매도')
elif ripple == 500:
    print('ripple 매수가 근접')
else:
    print('ripple 매수')
print('무조건 출력')


""" and 조건 테스트 """
bitcoin_ma5 = 1900
bitcoin_price = 1935
bitcoin_target = 1937

if (bitcoin_price >= bitcoin_ma5) and (bitcoin_price > bitcoin_target) :
    print("매수 상승장이고 변동성 돌파 전략 조건 만족")
    

""" 2.1.6 연습 문제 """
num1 = 10
num2 = 30

if num1 > num2 :
    print('num1이 더 큽니다')
elif num1 == num2 :
    print('num1과 num2가 같습니다.')
else:
    print('num2가 더 큽니다')
    
""" 2.1.6 연습 문제2 """
score = 84

if (score <= 100) and (score >= 90) :
    print('A 학점')
elif (score < 90) and (score >= 80) :
    print('B 학점')
elif (score < 80) and (score >= 70) :
    print('C 학점')
elif (score < 70) and (score >= 60) :
    print('D 학점')
elif (score < 60) and (score >= 50) :
    print('E 학점')
else:
    print('F 학점')
    
    
    
    