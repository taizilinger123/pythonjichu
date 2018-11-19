#!/usr/bin/env python
# -*- coding:utf-8 -*-
myStr = "hello world itcast and itcastxxxcpp"
myStr.find("world")
# myStr = "hello world itcast and itcastxxxcpp"
# myStr.find("world")
# Out[8]: 6
# myStr.find("dongge") #没有
# Out[9]: -1   #找不到
# myStr.find("itcast") #默认从左边找
# Out[10]: 12
# myStr.rfind("itcast")#从右边找
# Out[11]: 23
# myStr.index("world")
# Out[12]: 6
# myStr.index("dongge")#没有
# Traceback (most recent call last):
#   File "E:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-13-ff0fc6f1f683>", line 1, in <module>
#     myStr.index("dongge")
# ValueError: substring not found
# myStr.rindex("itcast")  #和find用法一样
# Out[14]: 23
# myStr.count("itcast")   #统计出现的次数
# Out[15]: 2
# myStr.count("dongge")   #没有
# Out[16]: 0
# myStr
# Out[17]: 'hello world itcast and itcastxxxcpp'  #元组，数字，字符串都是不可变的
# myStr.replace("world","WORLD")
# Out[18]: 'hello WORLD itcast and itcastxxxcpp'
# myStr
# Out[19]: 'hello world itcast and itcastxxxcpp'  #字符串都是不可变的
# myStr.replace("itcast","xxx")
# Out[20]: 'hello world xxx and xxxxxxcpp'        #都替换了
# myStr.replace("itcast","xxx",1)
# Out[21]: 'hello world xxx and itcastxxxcpp'     #从左往右替换第一个
# myStr
# Out[22]: 'hello world itcast and itcastxxxcpp'
# myStr.split(" ")                                #以空格切割字符串
# Out[23]: ['hello', 'world', 'itcast', 'and', 'itcastxxxcpp']
# myStr.capitalize()                              #首字母大写
# Out[24]: 'Hello world itcast and itcastxxxcpp'
# myStr.title()                                   #每个字母开头大写
# Out[25]: 'Hello World Itcast And Itcastxxxcpp'
# file_name = "xxxx.txt"
# file_name.endswith(".txt")                      #以....结尾
# Out[27]: True
# name = "wang xxxx"
# name.startswith("wang")                         #以....开头
# Out[29]: True
# myStr
# Out[30]: 'hello world itcast and itcastxxxcpp'
# myStr.lower()                                   #全部转为小写
# Out[31]: 'hello world itcast and itcastxxxcpp'
# myStr.upper()                                   #全部转为大写
# Out[32]: 'HELLO WORLD ITCAST AND ITCASTXXXCPP'
# lyric = "想要陪你一起看大海"
# lyric.center(50)
# Out[34]: '                    想要陪你一起看大海                     '  #左右空格50个
# lyric.ljust(50)
# Out[35]: '想要陪你一起看大海                                         '  #右边空格50个
# lyric.rjust(50)
# Out[36]: '                                         想要陪你一起看大海'  #左边空格50个
# test = lyric.center(50)
# test
# Out[38]: '                    想要陪你一起看大海                     '
# test.lstrip()
# Out[39]: '想要陪你一起看大海                     '                      #去掉左边的空格
# test.rstrip()
# Out[40]: '                    想要陪你一起看大海'                       #去掉右边的空格
# test.strip()
# Out[41]: '想要陪你一起看大海'                                           #去掉两边的空格
# myStr.rfind("itcast")                                                   #从右边开始找
# Out[44]: 23
# myStr.rindex("itcast")                                                  #从右边开始找
# Out[45]: 23
# myStr
# Out[46]: 'hello world itcast and itcastxxxcpp'
# myStr.partition("itcast")                        #以第一个itcast从左往右的往2边扩散
# Out[47]: ('hello world ', 'itcast', ' and itcastxxxcpp')
# myStr.rpartition("itcast")                       #以右边第一个itcast从右往左的往2边扩散
# Out[48]: ('hello world itcast and ', 'itcast', 'xxxcpp')
# test="hello\nworld\nxxx\nyy\nzz"
# test
# Out[50]: 'hello\nworld\nxxx\nyy\nzz'
# print(test)
# hello
# world
# xxx
# yy
# zz
# test.splitlines()
# Out[52]: ['hello', 'world', 'xxx', 'yy', 'zz']  #以换行\n分割字符串为列表
# num = input("请输入一个选项(1-6):")
# 请输入一个选项(1 - 6):q
# if num.isalpha():                      #判断是字母
#     print("是字母")
#
# 是字母
# if num.isdigit():                      #判断是数字
#     int(num)
#
# num = input("请输入一个选项(1-6):")
# 请输入一个选项(1 - 6):1q
# num.isalnum()                         #判断是数字和字母的组合
# Out[57]: True
# mystr = 'abc123'
# mystr.isspace()                       #判断里面包不包含空格
# Out[59]: False
# mystr = ''
# mystr.isspace()
# Out[61]: False
# mystr = ' '
# mystr.isspace()
# Out[63]: True
# a = ["aaa","bbb","cccc"]
# b = "="
# b.join(a)
# Out[66]: 'aaa=bbb=cccc'
# b = " "
# b.join(a)
# Out[68]: 'aaa bbb cccc'
# test = "aa s  \tgd  \ts a \tg\tlk  \tj\t  shijh  j \tl\t k g"
# test.split()
# Out[70]: ['aa', 's', 'gd', 's', 'a', 'g', 'lk', 'j', 'shijh', 'j', 'l', 'k', 'g']
# result = test.split()
# result
# Out[72]: ['aa', 's', 'gd', 's', 'a', 'g', 'lk', 'j', 'shijh', 'j', 'l', 'k', 'g']    #变成列表
# "".join(result)                                                                      #转变成字符串
# Out[73]: 'aasgdsaglkjshijhjlkg'
# names = ["老王","老李","老刘"]   #列表是处理相同的元素的
# names
# Out[76]: ['老王', '老李', '老刘']
# nums = [11,22,3.14,"100","laowang"]
# names
# Out[78]: ['老王', '老李', '老刘']
# names.append("老赵")
# names
# Out[80]: ['老王', '老李', '老刘', '老赵']
# names.insert(0,"八戒")
# names
# Out[82]: ['八戒', '老王', '老李', '老刘', '老赵']
# names2 = ["葫芦娃","叮当猫","猴子"]
# names
# Out[84]: ['八戒', '老王', '老李', '老刘', '老赵']
# names3 = names + names2
# names
# Out[86]: ['八戒', '老王', '老李', '老刘', '老赵']
# names3
# Out[87]: ['八戒', '老王', '老李', '老刘', '老赵', '葫芦娃', '叮当猫', '猴子']
# names2
# Out[88]: ['葫芦娃', '叮当猫', '猴子']
# names.extend(names3)
# names
# Out[90]:
# ['八戒',
#  '老王',
#  '老李',
#  '老刘',
#  '老赵',
#  '八戒',
#  '老王',
#  '老李',
#  '老刘',
#  '老赵',
#  '葫芦娃',
#  '叮当猫',
#  '猴子']
# names.pop()                              #删除最后的元素
# Out[92]: '猴子'
# names
# Out[93]: ['八戒', '老王', '老李', '老刘', '老赵', '八戒', '老王', '老李', '老刘', '老赵', '葫芦娃', '叮当猫']
# names
# Out[98]: ['八戒', '老王', '老李', '老刘', '老赵', '八戒', '老王', '老李']
# names.remove("老王")
# names
# Out[100]: ['八戒', '老李', '老刘', '老赵', '八戒', '老王', '老李']
# name = "laowang"
# name[0]
# Out[102]: 'l'
# names
# Out[103]: ['八戒', '老李', '老刘', '老赵', '八戒', '老王', '老李']
# names[0]
# Out[104]: '八戒'
# names[-1]
# Out[105]: '老李'
# names[2:5]
# Out[106]: ['老刘', '老赵', '八戒']
# del names[0]
# names
# Out[108]: ['老李', '老刘', '老赵', '八戒', '老王', '老李']
# names[0]
# Out[109]: '老李'
# names[0] = "沙师弟"
# names
# Out[111]: ['沙师弟', '老刘', '老赵', '八戒', '老王', '老李']
# if "老赵" in names:
#     print("找到了.....")
#
# 找到了.....
# if "老赵" not in names:
#     print("可以添加老赵....")
















