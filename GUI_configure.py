#  Copyright (c)

# import
import logging
import random
import sys
from collections import defaultdict
from datetime import datetime
# UI部分
from tkinter import *
from tkinter import messagebox

# 获取日志路径
from GUI_path import path
# 获取json定义的函数等
from sys_json import user_user_string as u_u_s
from sys_json import user_version_string as u_v_s
from sys_json import user_w_information_json as u_w_i_j

# 窗口配置
win_geometry = '320x180'
win_resizable = (False, False)

# 语言
language = {
    'population': '人口',
    'field': '土地',
    'money': '金钱'
}

# 抄作业
# 主窗口
# win = Tk()
# win.title('')
# win.iconbitmap('1.ico')
# win.geometry(win_geometry)
# win.resizable(win_resizable[0], win_resizable[1])

# 子窗口
# sub_window = Toplevel(win)
# sub_window.title("")
# sub_window.geometry(win_geometry)
# sub_window.iconbitmap('1.ico')
# sub_window.resizable(win_resizable[0], win_resizable[1])

# 日志初定义
if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# user_exit
def user_exit_page():
    logging.info('user exit page')
    if messagebox.askokcancel('exit page','真的要退出吗'):
        logging.info('True')
        logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        sys.exit()

    else:
        logging.info('False')


# 强制退出
def sys_exit(t_int: int):
    logging.debug(f'sys exit:{t_int}')
    sys.exit(t_int)


# 关闭窗口
def close_win(win: Tk):
    logging.info(f'window destroy')
    win.destroy()


# 关闭子窗口并解除主窗口隐藏
def close_win_deiconify(sub_window: Toplevel, win: Tk):
    logging.info(f'window destroy and deiconify window')
    sub_window.destroy()
    win.deiconify()


# 隐藏主窗口并绑定子窗口
def withdraw_win_sub_window(win: Tk, sub_window: Toplevel):
    logging.info('withdraw win')
    win.withdraw()
    sub_window.protocol("WM_DELETE_WINDOW", lambda: [sub_window.destroy(), win.deiconify()])


# 布置文本
def pack_message(win: Tk, t_text: str, t_width: int=300):
    logging.info(f'pack message:{t_text}')
    Message(win, text=t_text, width=t_width).pack()


# 布置按钮
def pack_button(win: Tk, t_text: str, t_command: defaultdict):
    logging.info(f'pack button:{t_text}\\{t_command}')
    Button(win, text=t_text, command=t_command).pack()


# 布置输入框
def pack_entry(win: Tk, t_width: int=50, t_if: bool=False, default_text: str=None):
    # default_text为默认文本(True)
    logging.info(f'pack enter:{t_if}\\{default_text}')
    entry = Entry(win, width=t_width)
    entry.pack()

    if t_if:
        # noinspection PyUnusedLocal
        def set_default_text(event=None):
            """当输入框失去焦点且为空时，设置默认文本"""
            if not entry.get():
                entry.insert(0, default_text)

        # noinspection PyUnusedLocal
        def clear_default_text(event=None):
            """当输入框获得焦点且有默认文本时，清除文本"""
            if entry.get() == default_text:
                entry.delete(0, END)

        # 默认文本
        entry.insert(0, default_text)

        # 绑定焦点事件
        entry.bind("<FocusIn>", clear_default_text)
        entry.bind("<FocusOut>", set_default_text)

    return entry


# 获取输入框
def get_entry(entry: Entry) -> str:
    t_str = entry.get()
    logging.info(f'get entry:{t_str}')
    return t_str


# 清空输入框
def delete_entry(entry: Entry):
    logging.info('entry delete')
    entry.delete(0, END)


# result页
def result_page():
    logging.info('game result page')
    if (u_u_s['name'] is not None and
            u_u_s['time'] is not None and
            u_u_s['result'] is not None and
            not u_u_s['result'] == 99):
        logging.info('True')

        win = Tk()
        win.title('result')
        win.iconbitmap('1.ico')
        win.geometry(win_geometry)
        win.resizable(win_resizable[0], win_resizable[1])

        pack_message(win,
                     t_text=f'上一次的用户名:{u_u_s['name']}\n上一次的用时:{u_u_s['time']}\n上一次的结局:{u_u_s['result']}',
                     t_width=300)
        pack_button(win,
                    t_text='确定',
                    t_command=lambda:close_win(win))

        win.mainloop()

    else:
        logging.info('False')
        messagebox.showerror('error', '未找到记录或记录有错误')

    logging.info('exit page\n')


# user页
def user_name_page():
    logging.info('user name page')
    if type(u_u_s['name']).__name__ == 'str' and not u_u_s['name'] == '':
        t_if = True
        logging.info('True name')
    else:
        t_if = False
        logging.info('False name')

    win = Tk()
    win.title('user name')
    win.iconbitmap('1.ico')
    win.geometry(win_geometry)
    win.resizable(win_resizable[0], win_resizable[1])

    def name(t_if: bool):
        if t_if:
            t_str = get_entry(entry)
            if t_str == '':
                logging.info('user name is None')
                messagebox.showerror('error', '名字不能为空')

            elif messagebox.askokcancel('yes?', f'确定要使用:"{t_str}"为名吗?'):
                logging.info(f'user name={t_str}')
                u_u_s['name'] = t_str
                close_win(win)

        elif not t_if:
            logging.info(f'reuse name:{u_u_s['name']}')
            close_win(win)

    entry = pack_entry(win, t_width=20, t_if=True, default_text='如何称呼你?')
    pack_button(win, t_text='确定', t_command=lambda: name(True))
    pack_button(win, t_text='清空', t_command=lambda: delete_entry(entry))
    if t_if:
        pack_button(win, t_text='复用', t_command=lambda: name(False))

    win.mainloop()

    u_w_i_j(u_u_s)
    logging.info('exit page\n')


# view resources页(查看资源)
def view_resources_page():
    logging.info('view resources page')

    win = Tk()
    win.title('view resources page')
    win.iconbitmap('1.ico')
    win.geometry(win_geometry)
    win.resizable(win_resizable[0], win_resizable[1])

    pack_message(win,
                 t_text=f'\n金钱:{u_v_s['money']}\n人口:{u_v_s["population"]}\n食物:{u_v_s["food"]}\n土地:{u_v_s["field"]}\n',
                 t_width=300)
    pack_button(win,
                t_text='确定',
                t_command=lambda: close_win(win))

    win.mainloop()

    logging.info('exit page\n')


# 商店页
def store_page():
    logging.info('store page')
    logging.info(f'relief food times={u_v_s['food_times']}')

    def store_a(string):
        logging.info(f'store:{string}')
        logging.info(f'money={u_v_s['money']}\\{string}={u_v_s[string]}')

        temp_max = u_v_s['money'] // u_v_s['price_' + string]

        def store_b(t_str: str):
            logging.info(f'user store:{t_str}')
            try:
                t_int = int(t_str)
                if t_int == 0:
                    messagebox.showinfo('info', '购买数不能为0')

                elif t_int > temp_max:
                    logging.info('False')
                    messagebox.showinfo('info', '钱不够')

                else:
                    u_v_s[string] += t_int
                    u_v_s['money'] -= u_v_s['price_' + string] * t_int
                    u_v_s['price_' + string] = int(u_v_s['price_' + string] * 1.05 // 1 + 1)
                    logging.info('True')
                    logging.info(f'money={u_v_s['money']}\\{string}={u_v_s[string]}')
                    messagebox.showinfo('store', f'购买成功\n目前持有{language[string]}:{u_v_s[string]}')
                    close_win_deiconify(sub_window, win)

            except ValueError:
                messagebox.showerror('error', '请输入正整数')
                delete_entry(entry)

            except Exception as e:
                logging.error(f'error \\ {e}')

        sub_window = Toplevel(win)
        sub_window.title(f'购买{language[string]}')
        sub_window.geometry(win_geometry)
        sub_window.iconbitmap('1.ico')
        sub_window.resizable(win_resizable[0], win_resizable[1])

        withdraw_win_sub_window(win, sub_window)
        pack_message(sub_window,
                     t_text=f'''目前持有金钱:{u_v_s['money']}\n目前持有{language[string]}:{u_v_s[string]}\n目前{language[string]}单价:{u_v_s["price_" + string]}\n最大可购买{language[string]}:{temp_max}''',
                     t_width=300)
        entry = pack_entry(sub_window,
                     t_width=20,
                     t_if=True,
                     default_text='整数')
        pack_button(sub_window,
                    t_text='确定购买',
                    t_command=lambda: store_b(get_entry(entry)))
        pack_button(sub_window,
                    t_text='清空输入',
                    t_command=lambda: delete_entry(entry))
        pack_button(sub_window,
                    t_text='退出购买',
                    t_command=lambda: close_win_deiconify(sub_window, win))

        sub_window.mainloop()

    # 救济食物
    def relief_food():
        logging.info(f'aid food\\times={u_v_s['food_times']}')

        if u_v_s['food_times'] >= 3:
            logging.info('False')
            messagebox.showinfo('aid food', '你已经没有机会领取了')

        elif u_v_s['food_times'] < 3:
            u_v_s['food'] += 500
            u_v_s['food_times'] += 1
            logging.info('True')
            messagebox.showinfo('aid food', '成功领取500食物')

    win = Tk()
    win.title('store page')
    win.iconbitmap('1.ico')
    win.geometry(win_geometry)
    win.resizable(win_resizable[0], win_resizable[1])

    pack_message(win, t_text=f'目前持有金钱:{u_v_s['money']}\n此提示不提供刷新', t_width=300)
    pack_button(win, t_text='购买人口', t_command=lambda: store_a('population'))
    pack_button(win, t_text='购买土地', t_command=lambda: store_a('field'))
    if u_v_s['food_times'] < 3:
        pack_button(win, t_text='食物救济', t_command=lambda: relief_food())

    pack_button(win, t_text='退出商店', t_command=lambda: close_win(win))

    win.mainloop()

    logging.info('exit page\n')


# event
def event_page():
    logging.info('event page')
    # 抉择,有利,不利
    # choice,advantageous,disadvantageous
    event_type = ["抉择", "有利", "不利"]
    event_choice = ["流浪商人来访", "交易", "money",
                    "逃难难民请求收留", "收留", "population",
                    "有一个投资机会", "投资", "money"]
    event_advantageous = ["非常难碰到的节日庆典", "money"]
    event_disadvantageous = ["自然灾害:地震", "自然灾害:干旱", "自然灾害:洪水", "自然灾害:泥石流", "自然灾害:火灾"]

    if random.randint(1, 100) <= 40:
        logging.info('False')
        messagebox.showinfo('event', '无事发生')

    else:
        temp = random.randint(0, 2)
        logging.info(f'True \\ type={event_type[temp]}')

        def resources(win: Tk, t_str: str, t_int: int, t_if: bool, t_random: int=100):
            logging.info(f'{t_str}\\{t_if}\\{t_int}')
            if t_if and random.randint(1, 100) <= t_random:
                logging.info(f'{t_str}\\+')
                u_v_s[t_str] += t_int
                messagebox.showinfo('event', f'{language[t_str]}增加了:{t_int}')

            else:
                logging.info(f'{t_str}\\-')
                u_v_s[t_str] -= t_int
                messagebox.showinfo('event', f'{language[t_str]}减少了:{t_int}')

            close_win(win)

        win = Tk()
        win.title('event page')
        win.iconbitmap('1.ico')
        win.geometry(win_geometry)
        win.resizable(win_resizable[0], win_resizable[1])

        pack_message(win, t_text=f'{event_type[temp]}类型事件')

        if temp == 0:
            temp = random.randint(0, (len(event_choice) - 1) // 3 - 1) * 3
            temp_list = [event_choice[temp], event_choice[temp + 1], event_choice[temp + 2]]
            logging.info(temp_list)

            if temp_list[2] == 'money':
                t_random = random.randint(50, 300)
            elif temp_list[2] == 'population':
                t_random = random.randint(10, 50)
            logging.info(f'random = {t_random}')

            pack_message(win, t_text=f'{temp_list[0]}')
            pack_button(win,
                        t_text=f'{temp_list[1]}',
                        t_command=lambda: resources(win,
                                                    t_str=temp_list[2],
                                                    t_int=t_random,
                                                    t_if=True,
                                                    t_random=60))

        elif temp == 1:
            temp = random.randint(0, (len(event_advantageous)) // 2 - 1) * 2
            temp_list = [event_advantageous[temp], event_advantageous[temp + 1]]
            logging.info(temp_list)
            if temp_list[1] =='money':
                temp = random.randint(100, 500)

            u_v_s[temp_list[1]] += temp
            logging.info(f'random = {temp}')

            pack_message(win, t_text=f'{temp_list[0]}\n{language[temp_list[1]]}增加了:{temp}')

        elif temp == 2:
            temp = random.randint(0, (len(event_disadvantageous) - 1))
            temp_list = [event_disadvantageous[temp]]

            pack_message(win, t_text=f'{temp_list[0]}')

            temp = random.randint(50, 300)
            u_v_s['money'] -= temp
            logging.info(f'money - {temp}')

            pack_message(win, t_text=f'金钱减少了:{temp}')

            temp = random.randint(10, 50)
            u_v_s['population'] -= temp
            logging.info(f'population - {temp}')

            pack_message(win, t_text=f'人口减少了:{temp}')

        else:
            logging.debug(f'type={temp}')
            messagebox.showerror('error', '事件类型超出范围')

        pack_button(win, t_text='确定', t_command=lambda: close_win(win))

        win.mainloop()

    logging.info('exit page\n')


# 结算页
def settlement_page():
    logging.info('settlement_page')
    # 资源结算
    u_v_s['money'] += u_v_s['population']
    u_v_s['food'] += u_v_s['field']

    if u_v_s['food'] >= u_v_s['population']:
        u_v_s['food'] -= u_v_s['population']

    else:
        u_v_s['population'] -= u_v_s['population'] - u_v_s['food']
        u_v_s['food'] = 0
        logging.info('food < 0')

        messagebox.showinfo('info', '食物不足,请尽快补充食物')

    u_u_s['time'] += 1

    # 结束判定
    result_if = True
    if u_v_s['money'] >= u_v_s['Victory conditions_money']:
        u_u_s['result'] = 0

    elif u_v_s['population'] >= u_v_s['Victory conditions_population']:
        u_u_s['result'] = 1

    elif u_v_s['food'] >= u_v_s['Victory conditions_food_Multiplier'] * u_v_s['population']:
        u_u_s['result'] = 2

    elif u_v_s['food'] < 0:
        u_u_s['result'] = 8

    elif u_v_s['population'] < 0:
        u_u_s['result'] = 9

    else:
        result_if = False

    return result_if


logging.info('configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

# 此内容应在传播前批量行注释掉
# if __name__ == '__main__':
    # user_exit_page()
    # result_page()
    # user_name_page()
    # view_resources_page()
    # store_page()
    # event_page()
    # settlement_page()
    # pass
