import socket
import threading


def handle_client(socket2, client_addr):
    """处理单个客户端的通信（放在前面定义）"""
    print(f"开始服务客户端: {client_addr}")

    while True:
        try:
            msg = socket2.recv(1024).decode('utf-8')
            if not msg or msg == 'quit':
                break

            print(f'来自{client_addr}的消息: {msg}')

            # 回复客户端
            send_msg = input(f'回复{client_addr}>>>')
            socket2.send(send_msg.encode('utf-8'))

        except Exception as e:
            print(f"客户端{client_addr}异常: {e}")
            break

    print(f"客户端{client_addr}断开连接")
    socket2.close()


def main():
    """主函数"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用（可选，避免重启报错）
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('', 8000))
    server_socket.listen(128)
    print("服务端启动，等待连接...")

    while True:
        # 循环接受新客户端
        socket2, client_addr = server_socket.accept()
        print(f"新客户端连接: {client_addr}")

        # 为每个客户端创建独立线程
        t = threading.Thread(target=handle_client, args=(socket2, client_addr))
        t.daemon = True  # 守护线程，主线程结束则结束
        t.start()


if __name__ == '__main__':
    main()