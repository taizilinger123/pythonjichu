f = open("test.txt", "r")
String =f.readline()

position = String.rfind("planSummary")
new_file_name = String[:position]
new1_file_name = String.split(" ")[-1]

print(new_file_name+new1_file_name)
f.close()