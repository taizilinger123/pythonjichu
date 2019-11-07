<<<<<<< HEAD
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

=======
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

>>>>>>> 4597e8de6d0b674fb3f44a7b50aa59f9c43ad005
print(soup.html)