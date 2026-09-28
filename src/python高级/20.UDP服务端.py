import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('',6666))

# recvfrom是阻塞函数 没有收到消息 程序会一直暂停不动
while True:
    msg,addr=server_socket.recvfrom(1024*10)
    print(f'来自客户端IP:{addr[0]},端口号;{addr[1]}的消息:{msg.decode('utf8')}')
    if msg.decode('utf8') == 'quit':
        break

    send_msg = input('服务端>>>')
    #  sendto 发送的数据不能是字符串 只能是字节数据
    server_socket.sendto(send_msg.encode('utf8'),addr)
    
server_socket.close()