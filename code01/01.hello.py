# coding:utf-8
class Bar(object):
    pass


class Foo(object): # 类之间要空2个空格，类名首字母大写
    """"""
    def __init__(self):
        pass

    def __getattr__(self, item):
        print item,
        # hello_world
        return  self

    def __str__(self): #需要返回值
        return ""

    def say_hello(self): #变量以下划线命名,不要用sayHello,遵循pep8规则
        pass

# obj = Foo()
# "think" obj.think
# obj.different

print(Foo().think.different.itcast)  #打上断点（Step Into）F7

# think different itcast


