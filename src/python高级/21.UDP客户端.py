import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 客户端
while True:
    send_msg = input('客户端>>>')
    if send_msg=='quit':
        client_socket.sendto(send_msg.encode('utf8'), ('192.168.3.199', 6666))
        break

    # 客户端需要指定目标地址和端口号
    client_socket.sendto(send_msg.encode('utf8'),('192.168.3.199',6666))
    # 接受服务器发过来的数据
    msg,addr = client_socket.recvfrom(1024*10)
    print(f'来自服务端IP:{addr[0]},端口号;{addr[1]}的消息:{msg.decode('utf8')}')


client_socket.close()

