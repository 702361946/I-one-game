#  Copyright (c)

# import
import logging
import sys
from datetime import datetime

# 获取日志路径
from LocalLow_log import path
# 获取json定义的函数等
from sys_json import user_user_string as u_u_s
from sys_json import user_w_information_json as u_w_i_j

# from sys_json import user_version_string as u_v_s

# 日志初定义
if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# user_exit
def user_exit():
    while True:
        temp = input('\n0 exit(退出)\n1 continue(返回)\n')
        if temp == '0':
            logging.info('user exit')
            sys.exit(0)
        elif temp == '1':
            logging.info('user exit continue')
            break
        else:
            print('请输入正确的值')


# 强制退出
def sys_exit():
    logging.debug('sys exit')
    sys.exit()


# result页
def game_result_page():
    logging.info('game_result_page')
    if u_u_s['name'] is not None and u_u_s['time'] is not None and u_u_s['result'] is not None:
        print(f'\n上一次的用户名为{u_u_s['name']}\n上一次的用时{u_u_s['time']}\n上一次的结局为{u_u_s['result']}')
        print('注:请自行对照结局表')
        logging.info('True')
    else:
        print('未找到信息')
        input('按下回车(Enter)继续')
        logging.info('False')


# user页
def game_user_page():
    logging.info('user_page')
    t = 0
    while True:
        temp = input('输入您的用户名\n输入up以复用用户名')
        logging.info(f'{t} user name={temp}')
        if temp == 'up':
            break

        elif input(f'确定使用"{temp}"作为用户名吗?(y/n)') == 'y':

            u_u_s['name'] = temp
            u_w_i_j(u_u_s)

            print(f'hello:{u_u_s['name']}')
            break

        else:
            t += 1

    logging.info(f'user name={u_u_s['name']}')


logging.info('configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
