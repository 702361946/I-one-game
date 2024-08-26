#  Copyright (c)

import logging
from datetime import datetime

# 获取日志路径
from LocalLow_log import path
# 配置
from sys_json import user_version_string as u_v_s
from sys_json import user_w_version_json as u_w_v_j

# 日志
if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
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
            temp = input(f'请输入新的{temp_str}的值')
            temp = int(temp)
            u_v_s[temp_str] = temp
            print('ok')
            logging.info(f'modify \\ ok \\ {temp_str}={u_v_s[temp_str]} \\ user_input={temp}')

        except Exception as e:
            print(f'error {e}')
            logging.error(f'error \\ {e}')

    except Exception as e:
        print(f'error {e}')
        logging.error(f'error \\ {e}')


def modifier():
    logging.info('modifier')

    vc_list = ['Victory conditions_money', 'Victory conditions_population', 'Victory conditions_food_Multiplier']

    resources_list = ['money', 'population', 'food', 'field', 'field_max', 'price_population', 'price_field']
    r_l = resources_list

    while True:
        temp = input(f'0 resources\n1 Victory conditions\n8 Save to File\n9 Save and Exit\n')

        if temp == '0':
            temp = input(f'0 {r_l[0]}\n1 {r_l[1]}\n2 {r_l[2]}\n3 {r_l[3]}\n4 {r_l[4]}\n5 {r_l[5]}\n6 {r_l[6]}\n9 Nix')
            if '6' >= temp >= '0':
                modify(r_l[int(temp)])

            elif temp == '9':
                pass

            else:
                print('请输入正确的值')

        elif temp == '1':
            print('Victory conditions')
            temp = input(f'0 money\n1 population\n2 food_Multiplier\n9 Nix')
            if '2' >= temp >= '0':
                modify(vc_list[int(temp)])

            elif temp == '9':
                pass

            else:
                print('请输入正确的值')

        elif temp == '8':
            u_w_v_j(u_v_s)
            print('ok')

        elif temp == '9':
            return u_v_s


logging.info('modifier ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
