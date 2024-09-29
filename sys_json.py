#  Copyright (c)

import json
import logging
from datetime import datetime

# 获取日志路径
from path import path

if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'sys_json'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

sys_version_string = {
    'money': 1000,
    'population': 100,
    'food': 100,
    'field': 100,
    'field_max': 5000,
    'price_population': 10,
    'price_field': 10,
    'food_times': 0,
    'Victory conditions_money': 10000,
    'Victory conditions_population': 1000,
    'Victory conditions_food_Multiplier': 100,
    'event': 9
}

logging.info('sys_version_string ok')
logging.info(f'sys_version_string=\n{sys_version_string}')

# 读用户定义的配置
try:
    with open('json/user_version.json', 'r+') as f:
        user_version_string = json.load(f)
        logging.info('user_version_string ok')
        logging.info(f'user_version_string=\n{user_version_string}')

except Exception as e:
    print(f'error {e}')
    logging.error(f'error {e}')
    user_version_string = sys_version_string


# 使用json.dump()将字典写入到文件中
def user_w_version_json(user_version_string):
    try:
        with open('json/user_version.json', 'w+') as f:
            json.dump(user_version_string, f, indent=4)

    except Exception as e:
        print(f'error {e}')
        logging.error(f'error {e}')


logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

logging.info('open user')

# user
sys_user_string = {
    'name': '',
    'time': 1,
    'result': 99
}

logging.info('sys_user_string ok')

try:
    with open('json/user.json', 'r+') as f:
        user_user_string = json.load(f)
        logging.info('user ok')
        logging.info(f'user=\n{user_user_string}')

except Exception as e:
    print(f'error {e}')
    logging.info(f'error {e}')
    user_user_string = sys_user_string


# 用户名等(u_u_s)
def user_w_information_json(user_user_string):
    try:
        with open('json/user.json', 'w+') as f:
            json.dump(user_user_string, f, indent=4)
        logging.info('w user_user_string ok')

    except Exception as e:
        print(f'error {e}')
        logging.error(f'error {e}')


# 存档部分
try:
    with open('json/save.json', 'r+') as f:
        save = json.load(f)
        if save[0] is True:
            save_u_u_s = save[1]
            save_u_v_s = save[2]
        logging.info('r record ok')
        logging.info(f'record=\n{save}')

except Exception as e:
    print(f'error {e}')
    logging.info(f'error {e}')


def save_w():
    logging.info('record')
    temp = [True, user_user_string, user_version_string]
    try:
        with open('json/save.json', 'w+') as f:
            json.dump(temp, f, indent=4)
        logging.info('record ok')
        print('保存完成')

    except Exception as e:
        print(f'error {e}')
        logging.error(f'error {e}')


logging.info('json ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
