# f = open("test.txt", "r")
# String =f.readline()
#
# position = String.rfind("planSummary")
# new_file_name = String[:position]
# new1_file_name = String.split(" ")[-1]
#
# print(new_file_name+new1_file_name)
# f.close()

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"),"html.parser")

soup = BeautifulSoup("<html>data</html>","html.parser")

print(soup.html)