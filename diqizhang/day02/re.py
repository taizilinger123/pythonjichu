python里re模块有两种方式：

#将正则表达式编译成一个pattern规则对象.
pattern = re.compile("\d+")

pattern.match():从开始位置开始往后查找，返回第一个符合规则的，只匹配一次
pattern.search():从任何位置开始往后查找，返回第一个符合规则的，只匹配一次
pattern.findall():所有的全部匹配，返回列表
#pattern.finditer():所有的全部匹配，返回的是一个迭代器
pattern.split():分割字符串，返回列表
pattern.sub():替换

match(str,begin,end)

re.I 表示忽略大小写
re.S 表示全文匹配

search(str,begin,end)

findall(str, begin, end)

split(str,count)

<div class="f18 mb20">
........
</div>

pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
content_list = pattern.findall(html)

