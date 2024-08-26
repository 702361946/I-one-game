#  Copyright (c)

# import
import logging
import sys
from datetime import datetime

# 获取日志路径
from LocalLow_log import path
# 获取json定义的函数等
from sys_json import user_user_string as u_u_s
from sys_json import user_version_string as u_v_s
from sys_json import user_w_information_json as u_w_i_j

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
    logging.info('user exit')
    while True:
        temp = input('\n0 exit(退出)\n1 continue(返回)\n')
        if temp == '0':
            logging.info('user exit')
            sys.exit(0)
        elif temp == '1':
            logging.info('user exit continue\n')
            break
        else:
            print('请输入正确的值')


# 强制退出
def sys_exit():
    logging.debug('sys exit')
    sys.exit()


# result页
def result_page():
    logging.info('game_result_page')
    if u_u_s['name'] is not None and u_u_s['time'] is not None and u_u_s['result'] is not None:
        print(f'\n上一次的用户名为{u_u_s['name']}\n上一次的用时{u_u_s['time']}\n上一次的结局为{u_u_s['result']}')
        print('注:请自行对照结局表')
        input('按下回车(Enter)继续')
        logging.info('True')
    else:
        print('未找到信息')
        input('按下回车(Enter)继续')
        logging.info('False')

    logging.info('exit page\n')


# user页
def user_page():
    logging.info('user_page')
    t = 0
    while True:
        temp = input('输入您的用户名\n输入up以复用用户名')
        logging.info(f'{t} user name={temp}')
        if temp == 'up':
            break

        elif temp == '':
            print('不能使用空气作为用户名!')
            t += 1

        elif input(f'确定使用"{temp}"作为用户名吗?(y/n)') == 'y':

            u_u_s['name'] = temp
            u_w_i_j(u_u_s)

            print(f'hello:{u_u_s['name']}')
            break

        else:
            t += 1

    logging.info(f'user name={u_u_s['name']}')
    logging.info('exit page\n')


# view resources页(查看资源)
def view_resources_page():
    logging.info('view resources page')
    print(f'\n金钱:{u_v_s['money']}\n人口:{u_v_s["population"]}\n食物:{u_v_s["food"]}\n土地:{u_v_s["field"]}\n')
    input('按下回车(Enter)继续')
    logging.info('exit page\n')


# 商店页
def stop_page():
    logging.info('stop page')
    # logging.info(f'food_times={food_times}')

    def stop_w(string):
        logging.info(f'stop:{string}')
        logging.info(f'money={u_v_s['money']}\\{string}={u_v_s[string]}')
        l_zh = {
            'population': '人口',
            'field': '土地',
        }
        temp_max = u_v_s['money'] // u_v_s['price_' + string]
        print(f'目前持有金钱:{u_v_s['money']}\n目前持有{l_zh['string']}:{u_v_s[string]}\n'
              f'目前{l_zh['string']}单价:{u_v_s["price_" + string]}')

        while True:
            temp = input(f'最大可购买{temp_max}\n输入你要的数量(整数)')
            logging.info(f'user input={temp}')
            try:
                temp = int(temp)
                if temp == 0:
                    print('购买数不可为0')

                elif temp <= temp_max:
                    u_v_s[string] += temp
                    u_v_s['money'] -= u_v_s['price_' + string] * temp
                    print(f'购买成功\n目前持有金钱:{u_v_s["money"]}\n目前持有{l_zh['string']}:{u_v_s[string]}')
                    u_v_s['price_' + string] *= 1.05
                    logging.info('True')
                    logging.info(f'money={u_v_s['money']}\\{string}={u_v_s[string]}')
                    break

                elif temp > temp_max:
                    print('钱不够')
                    logging.info('False')

            except Exception:
                print('输整数!')

    while True:
        print(f'目前持有金钱:{u_v_s['money']}')
        temp = input('\n0 人口\n1 土地\n2 救济食物(没做完)\n9 退出商店\n')

        if temp == '0':
            stop_w('population')

        elif temp == '1':
            stop_w('field')

        # elif temp == '2':
        #     logging.info(f'stop food times={food_times}')
        #     if food_times == 3:
        #         print('你没机会领了')
        #         logging.info('False')
        #
        #     elif food_times < 3:
        #         print('一次500食物')
        #         u_v_s['food'] += 500
        #         food_times += 1
        #         logging.info('True')

        elif temp == '9':
            break

        else:
            print('请输入正确的值')

    logging.info('exit page\n')
    # return food_times


logging.info('configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
