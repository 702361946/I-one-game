#  Copyright (c)

import logging
from datetime import datetime

from game import u_v_s
from sys_json import user_w_version_json

# 日志
if True:
    logging.basicConfig(filename='game.log', filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'modifier'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def modify(temp_str):
    logging.info(f'def modify \\ temp_str={temp_str}')
    try:
        print(f'\n{temp_str}目前的值:{u_v_s[temp_str]}')
        try:
            temp = int(input(f'请输入新的{temp_str}的值'))
            u_v_s[temp_str] = temp
            print(u_v_s[temp_str])

        except ExceptionGroup as e:
            print(f'error {e}')
            logging.error(f'error \\ {e}')

    except ExceptionGroup as e:
        print(f'error {e}')
        logging.error(f'error \\ {e}')


def modifier():
    logging.info('modifier')

    s_list = ['money', 'population', 'food', 'field', 'field_max', 'price_population', 'price_field',
              'Victory conditions_money', 'Victory conditions_population', 'Victory conditions_food_Multiplier']

    while True:
        temp = input(f'0 {s_list[0]}\n1 {s_list[1]}\n2 {s_list[2]}\n3 {s_list[3]}\n4 {s_list[4]}\n5 {s_list[5]}\n'
                     f'6 {s_list[6]}\n7 Victory conditions\n8 Save to File\n9 Save and Exit\n')

        if '6' >= temp >= '0':
            modify(s_list[int(temp)])

        elif temp == '7':
            print('Victory conditions')
            temp = input(f'0 money\n1 population\n2 food_Multiplier\n')
            if '2' >= temp >= '0':
                modify(s_list[int(temp) + 7])

            else:
                print('请输入正确的值')

        elif temp == '8':
            user_w_version_json(u_v_s)

        elif temp == '9':
            return u_v_s
