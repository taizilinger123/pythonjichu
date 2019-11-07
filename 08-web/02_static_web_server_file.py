#coding:utf-8
import socket
import re
from  multiprocessing import Process

# 设置静态文件根目录,常量全部要大写
HTML_ROOT_DIR = "./html"

def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request data:", request_data)
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)

    # 解析请求报文
    # 'GET /HTTP/1.1'
    request_start_line = request_lines[0]
    # 提取用户请求的文件名
    print("*"*10)
    print(request_start_line.decode("utf-8"))
    file_name = re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"

    # 打开文件，读取内容
    try:
        file = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server:My server\r\n"
        response_body = "The file is not found!"
    else:
        file_data = file.read()
        file.close()

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server:My server\r\n"
        response_body = file_data.decode("utf-8")

    response = response_start_line+response_headers+"\r\n"+response_body
    print("response data:",response)

    # 向客户端返回响应数据  ###注释的#和后面的字体之间留一个空格
    client_socket.send(bytes(response,"utf-8")) #python3 bytes

    # 关闭客户端连接
    client_socket.close()

if  __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("",8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        # print("[%s,%s]用户连接上了" %(client_address[0],client_address[1]))
        #ctrl+d复制当前行到下一行
        print("[%s,%s]用户连接上了" %client_address)
        # 光标放到hand_client上按alt+enter就会自动创建函数
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()

    # In[1]: s = "GET / HTTP/1.1\r\nHost:127.0.0.1:8000\r\nConnection: keep-alive"
    #
    # In[2]: s.splitlines()
    # Out[2]: ['GET / HTTP/1.1', 'Host:127.0.0.1:8000', 'Connection: keep-alive']
    #
    # In[3]:import re
    #
    # In[4]: re.match(r"\w+ +(/[^ ]*) ", "GET / HTTP/1.1").group(1)
    # Out[4]: '/'
    #
    # In[5]: re.match(r"\w+ +(/[^ ]*) ", "GET /index.html  HTTP/1.1").group(1)
    # Out[5]: '/index.html'