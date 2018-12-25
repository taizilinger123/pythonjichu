# coding:utf-8
class Bar(object):
    pass


class Foo(object): # 类之间要空2个空格，类名首字母大写
    """"""
    def __init__(self):
        self.itcast = 10

    def __getattr__(self, item):
        print item,
        # hello_world
        return  self

    def __getattribute__(self, item):
        return self.itcast   #死循环
        # self.__getattribute__("itcast")

    def __str__(self): # 需要返回值
        return ""


# obj = Foo()
# "think" obj.think
# obj.different

print(Foo().think)




