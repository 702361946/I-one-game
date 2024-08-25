#  Copyright (c)

# 备注
# 尝试尝试ConfigManager()

# import
try:
    from configure import *
    from modifier import modifier

    # 获取日志路径
    from LocalLow_log import path

except Exception as e:
    print(f'error {e}')
    input('exit(Enter)')
    exit(1)

# 日志初定义
if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'game'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# 定义补充

# 内容
print('hello')

while True:
    temp = input('\n0 开始\n1 记录\n2 修改器\n9 退出\n')
    if temp == '0':
        game_user_page()
        break

    elif temp == '1':
        game_result_page()

    elif temp == '2':
        u_v_s = modifier()

    elif temp == '9':
        user_exit()

    else:
        print('请输入正确的值')
