#  Copyright (c)
import logging

# 备注
# 尝试尝试ConfigManager()

# import
try:
    from GUI_configure import *
    from modifier import modifier

    # 获取日志路径
    from GUI_path import path

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


if True:
    time = 0
    time_settlement_if = False
    result_if = False
    logging.info('sys Initialization successful')


# 开始a
def game_a():
    win = Tk()
    win.title('game')
    win.iconbitmap('1.ico')
    win.geometry(win_geometry)
    win.resizable(win_resizable[0], win_resizable[1])

    pack_message(win, t_text='UI版本暂不提供存档\n修改器请看控制台')
    pack_button(win, t_text='开始游戏', t_command=lambda: [close_win(win), user_name_page()])
    pack_button(win, t_text='查看记录', t_command=lambda: result_page())
    pack_button(win, t_text='修改器', t_command=lambda: modifier())
    pack_button(win, t_text='退出游戏', t_command=lambda: user_exit_page())

    win.mainloop()
    # 初始化
    u_u_s['time'] = 0


# 主游戏框架
def game_b(u_u_s, u_v_s):
    global t_if
    # event
    if True:
        logging.info(f'event_open={u_v_s["event_open"]}')
        if u_v_s['event_open'] == 0:
            logging.info('event open')
            event_page()

        else:
            logging.info('event close')
            print('事件未启用')

    def game_round(win):
        logging.info('user Next round')
        global t_if
        t_if = settlement_page()
        close_win(win)
        logging.info('time->')

    win = Tk()
    win.title('game')
    win.iconbitmap('1.ico')
    win.geometry(win_geometry)
    win.resizable(win_resizable[0], win_resizable[1])

    pack_message(win,
                 t_text=f'回合{u_u_s['time']}')
    pack_button(win,
                t_text=f'资源查看',
                t_command=lambda: view_resources_page())
    pack_button(win,
                t_text=f'商店',
                t_command=lambda: store_page())
    pack_button(win,
                t_text=f'下一回合',
                t_command=lambda: game_round(win))
    pack_button(win,
                t_text=f'退出游戏',
                t_command=lambda: user_exit_page())

    win.mainloop()
    return t_if, u_u_s, u_v_s


if __name__ == '__main__':
    # a页
    if True:
        game_a()
        pass

    # b页
    if True:
        t_if = False
        u_u_s['time'] = 1
        while True:
            t_if, u_u_s, u_v_s = game_b(u_u_s, u_v_s)
            if t_if:
                logging.info('exit game_b')
                u_w_i_j(u_u_s)
                break
        pass

    # 游戏结束
    if True:
        win = Tk()
        win.title('game')
        win.iconbitmap('1.ico')
        win.geometry(win_geometry)
        win.resizable(win_resizable[0], win_resizable[1])

        pack_message(win, t_text='游戏结束')

        if u_u_s['result'] is not None and u_u_s['result'] <= 5:
            pack_message(win, t_text=f'你赢了\n结局为{u_u_s['result']}')
            logging.info('user win')

        else:
            pack_message(win, t_text=f'你输了\n结局为{u_u_s['result']}')
            logging.info('user no win')

        pack_message(win, t_text='请自行对照结局表')
        pack_button(win, t_text='结束游戏', t_command=lambda: [close_win(win), sys_exit(0)])

        u_w_i_j(u_u_s)

        win.mainloop()
