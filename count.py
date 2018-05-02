'''
Author:shiyongchao
Date: 2018/5/2
Describe:实现简单计算器:+,-,*,/
'''


class Calculator():
    '''
    实现两个数的加
    '''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b
