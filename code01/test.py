import  re
s = "WEA2BWEA23BA3BAA2BC4N5C6"
n = re.findall(r'A\dB|C\d', s)
print(n)
for  i  in n:
    print(i[1])