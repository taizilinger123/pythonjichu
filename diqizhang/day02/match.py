In [1]: import re

In [3]: pattern = re.compile(r"\d+")

In [4]: m = pattern.match("aaa123bbb456")

In [5]: print m
None

In [6]: m = pattern.match("aaa123bbb456",2,5)

In [7]: print m
None

In [8]: m = pattern.match("aaa123bbb456",3,5)//里面有多个字符串就m.group(1)

In [9]: print m
<_sre.SRE_Match object at 0x7f703de9de00>

In [10]: m.group()
Out[10]: '12'

In [11]: m = pattern.match("aaa123bbb456",3,6)

In [12]: m.group()
Out[12]: '123'

In [20]: pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)

In [21]: m = pattern.match("Hello world hello Python")

In [22]: m.group(0)
Out[22]: 'Hello world'

In [23]: m.group(1)
Out[23]: 'Hello'

In [24]: m.group(2)
Out[24]: 'world'

In [25]: m.span(1)
Out[25]: (0, 5)

In [26]: m.span(2)
Out[26]: (6, 11)
In [27]: pattern = re.compile(r"\d+")

In [28]: pattern.search(r"aaa123bbb456")
Out[28]: <_sre.SRE_Match at 0x7f703de9ded0>

In [29]: m = pattern.search(r"aaa123bbb456")

In [30]: m = pattern.search("aaa123bbb456")

In [31]: print m
<_sre.SRE_Match object at 0x7f703d81c030>

In [32]: print m.group()
123

In [33]: m = pattern.search("aaa123bbb456",2,5)

In [34]: print m.group()
12

In [35]: print m.span()
(3, 5)

In [36]: m = pattern.search("hello 123456 789")

In [37]: m.group()
Out[37]: '123456'

In [38]: m.span()
Out[38]: (6, 12)
In [39]: pattern = re.compile(r"\d+")

In [40]: pattern.findall("hello 123456 789")
Out[40]: ['123456', '789']

In [41]: pattern = re.compile(r"\d?")

In [42]: pattern.findall("hello 123456 789")
Out[42]: ['', '', '', '', '', '', '1', '2', '3', '4', '5', '6', '', '7', '8', '9', '']

In [43]: pattern = re.compile(r"\d*")

In [44]: pattern.findall("hello 123456 789")
Out[44]: ['', '', '', '', '', '', '123456', '', '789', '']

In [45]: pattern = re.compile(r"\d+")

In [46]: pattern.findall("hello 123456 789")
Out[46]: ['123456', '789']

In [47]: pattern.findall("aaa123bbb456", 1, 10)
Out[47]: ['123', '4']

In [48]: m = pattern.findall("aaa123bbb456", 1, 10)

In [49]: m
Out[49]: ['123', '4']

In [50]: for i in m:
   ....:      print i
   ....:     
123
4

In [51]: m = pattern.finditer("aaa123bbb456")

In [52]: m
Out[52]: <callable-iterator at 0x7f703d800890>

In [53]: for i  in m:
   ....:     print  i
   ....:     
<_sre.SRE_Match object at 0x7f703de9de00>
<_sre.SRE_Match object at 0x7f703d820098>

In [54]: for i  in m:
           print  i.group()
   ....:     

In [55]: m = pattern.finditer("aaa123bbb456")

In [56]: type(m)
Out[56]: callable-iterator

In [57]: for i in m:
   ....:     print i.group()
   ....:     
123
456

In [59]: pattern =  re.compile(r"[\s\d\\\;]+")

In [60]: m = pattern.split("a bb\aa;mm;    a")

In [61]: m
Out[61]: ['a', 'bb\x07a', 'mm', 'a']

In [62]: pattern = re.compile("[\s\d\\\;]+")

In [63]: m = pattern.split("a bb\aa;mm;    a")

In [64]: m
Out[64]: ['a', 'bb\x07a', 'mm', 'a']

In [65]: m = pattern.split(r"a bb\aa;mm;    a")

In [66]: m
Out[66]: ['a', 'bb', 'aa', 'mm', 'a']

In [67]: m = pattern.split(r"a bb\aa;m1m;  123  a")

In [68]: m
Out[68]: ['a', 'bb', 'aa', 'm', 'm', 'a']

In [69]: import re

In [70]: pattern = re.compile(r"(\w+)(\w+)")

In [71]: str = "hello 123, hello 456"

In [72]: m = pattern.sub("hello world", str)

In [73]: m
Out[73]: 'hello world hello world, hello world hello world'

In [74]: pattern.sub("\1 \2",str)
Out[74]: '\x01 \x02 \x01 \x02, \x01 \x02 \x01 \x02'

In [75]: m = pattern.sub("\1 \2",str)

In [76]: m = pattern.sub(r"\1 \2",str)

In [77]: m
Out[77]: 'hell o 12 3, hell o 45 6'

In [78]: m = pattern.sub(r"\2 \1",str)

In [79]: m
Out[79]: 'o hell 3 12, o hell 6 45'

In [80]: str
Out[80]: 'hello 123, hello 456'

In [81]: pattern = re.compile(r"\d+")

In [82]: str = "abc123abc456"

In [83]: pattern.sub(r"mmmm",str)
Out[83]: 'abcmmmmabcmmmm'

