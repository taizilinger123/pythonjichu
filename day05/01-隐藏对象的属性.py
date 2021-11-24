#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Dog:
    def set_age(self, new_age):
        if new_age>0 and new_age<=100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age

dog = Dog()
# dog.age = -10
# dog.name = "小白"
#print(dog.age)

dog.set_age(-10)
age = dog.get_age()
print(age)
# dog.get_name()

dog.age = -10
print(dog.age)


def __init__(self,name='',age=0):
       self._name=name;  #如果不该名的话会出错，所以改成._name
       self._age = age;    #同上
   @property         #要先有property才能有下面的setter方法
    def age(self):
       return self._age
   @age.setter
    def age(self,age):
       if age>0 and age<=150:
           self._age = age
   @property
    def name(self):
       return self._name
   @name.setter
    def name(self, name):
       self._name = name

Python中类的变量，一个下划线与两个下划线的区别：
__xx	这是私有变量， 只有内部可以访问，外部不可以访问。但是也不是一定不可以访问，只要以 _类名__xx样式就可以访问 。但最好不要这样做，养成良好编程习惯
_x	    这是实例变量，可以访问，但是不要轻易访问。按照约定俗成，当你看到这样的变量时，意思就是，“虽然我可以被访问，但请把我视为私有变量，不要随意访问”。
