#  Copyright (c)
import json
import logging
import os
import socket
import time
import uuid
from datetime import datetime

if True:
    path = os.path.expanduser('~\\AppData\\LocalLow\\702361946\\UDP\\B_S_game client_side.log')
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'client'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print('此程序需要您加入zerotier网络\n(id:60ee7c034a89b0d9)\n请确保您已加入\n否则可能出现错误')
while True:
    temp = input('您已加入zerotier?(y/n)')
    if temp == 'y':
        logging.info('User True')
        break

    elif temp == 'n':
        logging.info('User False')
        input('按下Enter退出程序')
        exit(0)

    else:
        print('请输入正确的值(y/n)')


try:
    with (open('user.json', 'r+') as f):
        record = json.load(f)
        logging.info(f'record={record}')
        if (not record['name'] == '' and
                type(record['name']).__name__ == 'str' and
                type(record['time']).__name__ == 'int' and
                type(record['result']).__name__ == 'int' and
                not record['result'] == 99):

            logging.info('record True')
            pass
        else:
            logging.info('record False')
            print('请确认记录无问题')
            input('按下Enter退出')
            exit()

except Exception as e:
    logging.error(f'error:{e}')
    input('error')
    exit()


# 创建UDP套接字
k_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
k_udp.setblocking(False)
logging.info('udp ok')

server_ip = ('192.168.191.100', 55000)
while True:
    try:
        k_udp.sendto('client -> server'.encode('utf-8'), server_ip)
        time.sleep(1)
        if (k_udp.recvfrom(1024))[0].decode('utf-8') == 'hello client':
            logging.info(f'server ip:{server_ip}')
            break

    except Exception:
        input('请检查是否加入了zerotier网络\n或检查网络连接\n或联系:702361946@qq.com')

# 4.发送数据
def send_data(data: str):
    logging.info(f'send {data}')
    try:
        k_udp.sendto(data.encode('utf-8'), server_ip)

    except Exception as e:
        print(f'error:{e}')


def recv(t_recv):
    print(t_recv)


# 5.主循环
temp_if = True
while True:
    if temp_if:
        temp = input('0 上传记录\n1 下载记录\n9 退出上传')

    else:
        print('退出')
        exit(0)

    if temp == '0' or temp == '1':
        try:
            def get_mac_address():
                mac = uuid.getnode() % 0x100000000
                mac = f'{mac:012x}'
                return ':'.join(mac[i:i + 2] for i in range(0, 12, 2))

            mac_id = get_mac_address()

            if temp == '0':
                send_data(
                    f'up record,mac_id={mac_id},name={record['name']},time={record['time']},result={record['result']}')
                time.sleep(1)
                recv_data = k_udp.recvfrom(1024)  # 1024表示本次接收的最大字节数
                recv(recv_data[0].decode("utf-8"))

            elif temp == "1":
                send_data(
                    f'download record,mac_id={mac_id}')
                time.sleep(1)
                recv_data = k_udp.recvfrom(1024)  # 1024表示本次接收的最大字节数
                recv(recv_data[0].decode("utf-8"))

        except ConnectionResetError:
            print('服务器已关闭或服务器不存在')

        except Exception:
            print('超时或其他')

    elif temp == '9':
        temp_if = False
        k_udp.close()
        break

    else:
        pass

logging.info('exit')
logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
