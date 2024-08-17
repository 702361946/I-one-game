#  Copyright (c)

# import
import logging
from datetime import datetime

# 日志初定义
if True:
    logging.basicConfig(filename='configure.log', filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# with
# result
try:
    with open('result.txt', 'r+', encoding='utf-8') as result_txt:
        for text in result_txt:
            result_list = text.split(';')
            result = int(result_list[0])
            result_max = int(result_list[1])
            time = int(result_list[3])
            logging.info(f'sys open result result={result}')
            if not 0 <= result <= result_max:
                result = False
                print('result not recognized')
                logging.error(f'sys open result error \\ result={result}')

except Exception as e:
    print(f'error {e}')
    result = False
    result_max = False
    time = None
    logging.error(f'sys open result error \\ {e} \\ result={result} \\ result.txt={text}')


def sys_w_result(result, result_max, time):
    try:
        if isinstance(result, int) and isinstance(result_max, int) and isinstance(time, int):
            with open('result.txt', 'w+', encoding='utf-8') as result_txt:
                result_txt.write(f'{result};{result_max};time;{time}')
                logging.info(f'user w result \\ ok')

        else:
            print('error result or result_max or time no int')
            logging.error(f'user w result not int \\ result={result} \\ result_max={result_max} \\ time={time}')

    except Exception as e:
        print(f'error {e}')
        logging.error(f'user def w_result error \\ {e}')


# user
try:
    with open('user.txt', 'r+', encoding='UTF-8') as user_txt:
        for text in user_txt:
            user_txt_split = text.split(';')
            user_name = user_txt_split[1]
            logging.info(f'sys open user user_name={user_name}')

except Exception as e:
    print(f'error {e}')
    user_name = None
    logging.error(f'sys open user error \\ {e}')


def sys_w_user(user_name):
    try:
        with open('user.txt', 'w+', encoding='UTF-8') as user_txt:
            user_txt.write(f'user;{user_name}')
            logging.info(f'user w user ok')

    except Exception as e:
        print(f'error {e}')
        logging.error(f'user w user error \\ {e}')
