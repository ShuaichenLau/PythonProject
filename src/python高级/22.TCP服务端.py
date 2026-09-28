import socket

# socket.AF_INET - 地址族（Address Family）
# | `AF_INET` | **IPv4** 地址（最常用的互联网协议） |
# | `AF_INET6` | IPv6 地址 |
# | `AF_UNIX` | 本地 Unix 域套接字（同一台机器进程间通信） |

# socket.SOCK_DGRAM - 套接字类型（Socket Type）
# | `SOCK_DGRAM` | **UDP** 协议（数据报） | 无连接、不可靠、速度快 |
# | `SOCK_STREAM` | **TCP** 协议（字节流） | 面向连接、可靠、有顺序保证 |

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server_socket.bind(('',8000))
# 服务器允许最大建立的个数
server_socket.listen(128)
# 接受客户端的连接
socket2,client_addr = server_socket.accept()

while True:
    msg = socket2.recv(1024).decode('utf8')
    print(f'来自客户端IP:{client_addr[0]},端口号;{client_addr[1]}的消息:{msg}')
    if msg == 'quit':
        socket2.send('byebye'.encode('utf8'))
        break
    # 给客户端发消息
    send_msg = input('服务器>>>')
    socket2.send(send_msg.encode('utf8'))

socket2.close()
server_socket.close()


