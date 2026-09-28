import socket

# socket.AF_INET - 地址族（Address Family）
# | `AF_INET` | **IPv4** 地址（最常用的互联网协议） |
# | `AF_INET6` | IPv6 地址 |
# | `AF_UNIX` | 本地 Unix 域套接字（同一台机器进程间通信） |

# socket.SOCK_DGRAM - 套接字类型（Socket Type）
# | `SOCK_DGRAM` | **UDP** 协议（数据报） | 无连接、不可靠、速度快 |
# | `SOCK_STREAM` | **TCP** 协议（字节流） | 面向连接、可靠、有顺序保证 |

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# TCP客户端不需要绑定端口号, 因为TCP客户端是主动发起连接
server_addr=('192.168.3.199',8000)
# '' 代表本地IP
client_socket.connect(server_addr)

while True:
    send_msg = input('客户端>>>')
    client_socket.send(send_msg.encode('utf8'))
    msg = client_socket.recv(1024).decode('utf8')
    print(f'来自服务端IP:{server_addr[0]},端口号;{server_addr[1]}的消息:{msg}')
    if msg == 'byebye':
        break

client_socket.close()