#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import time

class MyNewProcess(Process):
    def run(self):
        while True:
            print("-----1----")
            time.sleep(1)

p = MyNewProcess()
p.start()

while True:
    print("----main----")
    time.sleep(1)
    
    
    
先在~/.vimrc文件中设置一下参数，set shiftwidth=4。
之后进入vim中，按下v，进行选择移动的整段代码，是连续的代码段。之后进行可以  向左（向右）移动。
shift+> (向右缩进) ，shift+<(向左缩进)。
:10,100>
第10行至第100行缩进
:20,80<
第20行至第80行反缩进


然后按shift+v，此时，按键盘上的上下左右方向键，选中所有需要批量缩进的行,
选择好了之后，按shift+>,是向前缩进一个tab值，按shift+<，则是缩回一个tab值，
