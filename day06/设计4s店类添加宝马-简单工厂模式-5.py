#!/usr/bin/env python
# -*- coding:utf-8 -*-
class BMWCarStore(object):
    def __init__(self):
        self.factory = BMWFactory()

    def  order(self, car_type):
       return  self.factory.select_car_by_type(car_type)

class BMWFactory(object):
    def select_car_by_type(car_type):
        pass
        # if car_type=="mini":
        #     return Suonata()
        # elif car_type=="720li":
        #     return Mingtu()
        # elif car_type=="x6":
        #     return Ix35()



class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def  order(self, car_type):
       return  self.factory.select_car_by_type(car_type)

#解耦
class Factory(object):
    def select_car_by_type(car_type):
        if car_type=="索纳塔":
            return Suonata()
        elif car_type=="名图":
            return Mingtu()
        elif car_type=="ix35":
            return Ix35()

class Car(object):
    def move(self):
        print("车在移动....")
    def music(self):
        print("车在播放音乐....")
    def stop(self):
        print("车在停止....")

class Suonata(Car):
    pass

class Mingtu(Car):
    pass

class Ix35(Car):
    pass

car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()