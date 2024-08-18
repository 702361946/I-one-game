#  Copyright (c)

import json
import logging
from datetime import datetime

if True:
    logging.basicConfig(filename='game.log', filemode='w', level=logging.DEBUG, encoding='UTF-8')
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
    'Victory conditions_money': 10000,
    'Victory conditions_population': 1000,
    'Victory conditions_food_Multiplier': 1000
}

logging.info('sys_version_string ok')
logging.info(f'sys_version_string=\n{sys_version_string}')

# 读用户定义的配置
try:
    with open('user_version.json', 'r+') as f:
        user_version_string = json.load(f)
        logging.info('user_version_string ok')
        logging.info(f'user_version_string=\n{user_version_string}')

except ExceptionGroup as e:
    print(f'error {e}')
    logging.error(f'error {e}')
    user_version_string = sys_version_string


# 使用json.dump()将字典写入到文件中
def user_w_version_json(user_version_string):
    try:
        with open('user_version.json', 'w+') as f:
            json.dump(user_version_string, f, indent=4)

    except ExceptionGroup as e:
        print(f'error {e}')
        logging.error(f'error {e}')


logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

logging.info('open user')

# user
sys_user_string = {
    'name': None,
    'time': None,
    'result': None
}

logging.info('sys_user_string ok')

try:
    with open('user.json', 'r+') as f:
        user_user_string = json.load(f)
        logging.info('user ok')
        logging.info(f'user=\n{user_user_string}')

except ExceptionGroup as e:
    print(f'error {e}')
    logging.info(f'error {e}')
    user_user_string = sys_user_string


def user_w_information_json(user_user_string):
    try:
        with open('user.json', 'w+') as f:
            json.dump(user_user_string, f, indent=4)

    except ExceptionGroup as e:
        print(f'error {e}')
        logging.error(f'error {e}')


logging.info('exit')
logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))