#  Copyright (c)
import logging

# 备注
# 尝试尝试ConfigManager()

# import
try:
    from configure import *
    from modifier import modifier
    # 获取存档函数
    from sys_json import save_w
    # 获取存档内容
    from sys_json import save
    if save[0] is True:
        from sys_json import save_u_u_s, save_u_v_s

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
print('hello user')

while True:
    temp = input('\n0 开始\n1 记录\n2 修改器\n9 退出\n')
    if temp == '0':
        if input('加载进度?(y/n)') == 'y':
            if save[0] is True:
                u_u_s = save_u_u_s
                u_v_s = save_u_v_s
            else:
                print('加载失败')
                user_page()
        else:
            user_page()
        break

    elif temp == '1':
        result_page()

    elif temp == '2':
        u_v_s = modifier()

    elif temp == '9':
        user_exit()

    else:
        print('请输入正确的值')

# 初始化
time = 0
time_settlement_if = False
result_if = False
# food_times = 0
logging.info('sys Initialization successful')

# 主游戏框架
while True:
    time += 1
    # people to land
    p_t_l = round(u_v_s['field'] / u_v_s['population'], 2)
    print(f'回合{time}开始\n当前持有金钱{u_v_s['money']}\n人地比为:{p_t_l}')
    logging.info(f'time={time}\\money={u_v_s["money"]}\\population={u_v_s['population']}\\field={u_v_s['field']}')
    logging.info(f'event_open={u_v_s["event_open"]}')
    if u_v_s['event_open'] == 0:
        logging.info('event open')
        event_page()

    else:
        logging.info('event close')
        print('事件未启用')

    while True:
        temp = input(f'0 资源查看\n1 商店\n7 保存进度\n8 下一回合\n9 退出')

        if temp == '0':
            view_resources_page()

        elif temp == '1':
            stop_page()

        elif temp == '7':
            save_w()

        elif temp == '8':
            logging.info('user Next round')
            time_settlement_if = True

        elif temp == '9':
            user_exit()

        elif temp == 'modifier':
            modifier()

        else:
            print('请输入正确的值')

        # 结束结算
        if time_settlement_if is True:
            # 结算
            result_if = settlement_page()

            # 结算后
            time_settlement_if = False
            logging.info('time->')
            break

    if result_if is True:
        u_u_s['time'] = time
        logging.info(f'time={u_u_s['time']}\\result={u_u_s['result']}')
        break

# 游戏结束
if True:
    print('游戏结束')
    if u_u_s['result'] is not None and u_u_s['result'] <= 5:
        print(f'你赢了\n结局为{u_u_s['result']}')

    else:
        print(f'你输了\n结局为{u_u_s['result']}')

    print('请自行对照结局表')
    save_w()

input('按下回车(Enter)结束游戏')
