# @2024
# 开始时间2024-04-04
# 单人开发(702361946@qq.com)
# 版权所有，拒绝盗用
# 赋值
if True:
    import random
    import os
    from tkinter import *
    from tkinter import messagebox

    temporary = ''

    with open('event.txt', 'r', encoding='UTF-8') as event:
        for txt in event.readlines():
            txt = txt.split(';')
            event = int(txt[1])

    with open('user.txt', 'r', encoding='UTF-8') as user:
        for txt in user.readlines():
            txt = txt.split(';')
            version_Last = txt[1]
            user = txt[3]
            time = txt[5]
            vc = txt[7]

    with open('version.txt', 'r', encoding='UTF-8') as version:
        for txt in version.readlines():
            txt = txt.split(';')

            version = txt[0]
            money = int(txt[1])
            population = int(txt[2])
            population_price = int(txt[3])
            food = int(txt[4])
            field = int(txt[5])
            field_min = int(txt[6])
            field_max = int(txt[7])
            field_price = int(txt[8])
            vc_m = int(txt[9])
            vc_p = int(txt[10])
            vc_f_m = int(txt[11])
            language = int(txt[12])
            verification = txt[13]

    field_current = random.randint(field_min, field_max)
    vc_f = population * vc_f_m


    def vc_vc(vc):
        global temporary
        if vc == '0':
            temporary = ['上一次的胜利方式:金钱', 'The previous victory method:money']
        elif vc == '1':
            temporary = ['上一次的胜利方式:人口', 'The previous victory method:population']
        elif vc == '2':
            temporary = ['上一次的胜利方式:食物', 'The previous victory method:food']
        elif vc == '3':
            temporary = ['失败方式:被强盗杀死', 'Failure mode:Killed by bandits']
        elif vc == '4':
            temporary = ['失败方式:破产', 'Failure mode:bankruptcy']
        elif vc == '5':
            temporary = ['失败方式:集体死亡', 'Failure mode:Collective death']
        else:
            temporary = ['?', '?']

#  开始页
if True:
    if language == 0:
        txt0 = '退出游戏'
        txt1 = '设置'
        txt2 = '上一次的记录'
        txt3 = '开始'
    elif language == 1:
        txt0 = 'Exit the game'
        txt1 = 'Settings'
        txt2 = 'Last Record'
        txt3 = 'start'

    win0 = Tk()
    win0.title("tp_1")
    win0.geometry("320x180")
    win0.iconbitmap("1.ico")
    win0.resizable(False, False)


    def esc():
        os.abort()


    def settings():
        win1 = Tk()
        win1.title("settings")
        win1.geometry("320x180")
        win1.iconbitmap("1.ico")
        win1.resizable(False, False)

        if language == 0:
            txt0 = '语言'
            txt1 = '修改器'
            txt2 = '返回上一级'
        elif language == 1:
            txt0 = 'Language'
            txt1 = 'modifier'
            txt2 = 'Return to the previous level'

        def settings_language():
            win2 = Tk()
            win2.title("settings_language")
            win2.geometry("320x180")
            win2.iconbitmap("1.ico")
            win2.resizable(False, False)

            if language == 0:
                txt0 = '按下切换'
                txt1 = '确定'
            elif language == 1:
                txt0 = 'Press to switch'
                txt1 = 'ok'

            def settings_language_button():
                if language == 0:
                    temp = 1
                elif language == 1:
                    temp = 0

                txt = open('version.txt', 'w')
                txt.write(
                    version + ';' + str(money) + ';' + str(population) + ';' + str(
                        population_price) + ';' + str(
                        food) + ';' + str(field) + ';' + str(field_min) + ';' + str(field_max) + ';' + str(
                        field_price) + ';' + str(vc_m) + ';' + str(vc_p) + ';' + str(vc_f_m) + ';' + str(
                        temp) + ';' + str(verification))
                txt.close()

                os.abort()

            message0 = Message(win2, text=txt0, width=300)
            button0 = Button(win2, text=txt1, command=settings_language_button)

            message0.pack()
            button0.pack()

            win2.mainloop()

        def settings_modifier():
            os.system('start xg.exe')

        def settings_exit():
            win1.destroy()

        button0 = Button(win1, text=txt0, state=NORMAL, command=settings_language)
        button1 = Button(win1, text=txt1, state=NORMAL, command=settings_modifier)
        button2 = Button(win1, text=txt2, state=NORMAL, command=settings_exit)

        button0.pack()
        button1.pack()
        button2.pack()

        win1.mainloop()


    def record():
        win1 = Tk()
        win1.title("record")
        win1.geometry("320x180")
        win1.iconbitmap("1.ico")
        win1.resizable(False, False)

        vc_vc(vc)
        if language == 0:
            txt0 = ('上一次的版本:' + version_Last)
            txt1 = ('上一次的用户名:' + user)
            txt2 = ('上一次游戏总用时:' + time)
            txt3 = (temporary[0])
        elif language == 1:
            txt0 = ('Last version:' + version_Last)
            txt1 = ('Last username:' + user)
            txt2 = ('Last game total time:' + time)
            txt3 = (temporary[1])

        message0 = Message(win1, text=txt0, width=300)
        message1 = Message(win1, text=txt1, width=300)
        message2 = Message(win1, text=txt2, width=300)
        message3 = Message(win1, text=txt3, width=300)

        message0.pack()
        message1.pack()
        message2.pack()
        message3.pack()

        win1.mainloop()


    def start():
        win0.destroy()


    button0 = Button(win0, text=txt0, state=NORMAL, command=esc)
    button1 = Button(win0, text=txt1, state=NORMAL, command=settings)
    button2 = Button(win0, text=txt2, state=NORMAL, command=record)
    button3 = Button(win0, text=txt3, state=NORMAL, command=start)
    button3.pack()
    button2.pack()
    button1.pack()
    button0.pack()

    win0.mainloop()
#  user
if True:
    win0 = Tk()
    win0.title("user")
    win0.geometry("320x180")
    win0.iconbitmap("1.ico")
    win0.resizable(False, False)

    if language == 0:
        txt0 = '如何称呼您?'
        txt1 = '确定'
        txt2 = '清空'
    elif language == 1:
        txt0 = 'How do I address you?'
        txt1 = 'ok'
        txt2 = 'clear'

    def user_y():
        global user
        user = entry0.get()
        win0.destroy()
        user_open = open('user.txt', 'w', encoding='UTF-8')
        user_open.write('version;' + version)
        user_open.write(';user;' + user)
        user_open.write(';time;' + time)
        user_open.write(';Victory conditions;' + vc)
        user_open.close()

    def user_n():
        entry0.delete(0, 'end')

    message0 = Message(win0, text=txt0, width=320)
    entry0 = Entry(win0)
    entry0.insert(0, user)
    button0 = Button(win0, text=txt1, command=user_y)
    button1 = Button(win0, text=txt2, command=user_n)

    message0.pack()
    entry0.pack()
    button0.pack(side='left', padx=50, pady=50)
    button1.pack(side='left', padx=70, pady=0)

    win0.mainloop()
#  主游戏
t0 = 0
time = 1
while t0 < 1:

    win0 = Tk()
    win0.title("game")
    win0.geometry("320x180")
    win0.iconbitmap("1.ico")
    win0.resizable(False, False)

    if language == 0:
        txt0 = '退出游戏'
        txt1 = '下一回合'
        txt2 = '查看资源'
        txt3 = '商店'
    elif language == 1:
        txt0 = 'exit game'
        txt1 = 'Next round'
        txt2 = 'View Resources'
        txt3 = 'Store'


    def event_enable():
        win1 = Tk()
        win1.title("event")
        win1.geometry("320x180")
        win1.iconbitmap("1.ico")
        win1.resizable(False, False)

        def win1_esc():
            win1.destroy()

        def event_win1(txt0, txt1, txt2, button0_def, button1_def, temporary):
            message0 = Message(win1, text=txt0, width=300)
            button0 = Button(win1, text=txt1, command=button0_def)
            button1 = Button(win1, text=txt2, command=button1_def)

            message0.pack()
            button0.pack()
            if temporary == 1:
                button1.pack()

        random0 = random.randint(0, 4)
        if random0 == 0:
            if language == 0:
                txt0 = '无事发生'
                txt1 = '确定'
            elif language == 1:
                txt0 = 'Nothing'
                txt1 = 'ok'

            event_win1(txt0, txt1, txt1, win1_esc, win1_esc, 0)
        elif random0 == 1:
            if language == 0:
                txt0 = '有一群难民,请求您的收留'
                txt1 = '收留'
                txt2 = '赶走'
            elif language == 1:
                txt0 = 'There is a group of refugees requesting your accommodation'
                txt1 = 'retention'
                txt2 = 'Drive away'

            def event_random1():
                def event_refugee_enable(txt0):
                    win2 = Tk()
                    win2.title("event_refugee")
                    win2.geometry("320x180")
                    win2.iconbitmap("1.ico")
                    win2.resizable(False, False)

                    global population
                    population = population + random0

                    if language == 0:
                        txt1 = '确定'
                    elif language == 1:
                        txt1 = 'ok'

                    def event_refugee_ok():
                        win2.destroy()
                        win1.destroy()

                    def exit_game():
                        win2.destroy()
                        win1.destroy()
                        win0.destroy()

                    message0 = Message(win2, text=txt0)
                    button0 = Button(win2, text=txt1, command=event_refugee_ok)
                    button1 = Button(win2, text=txt1, command=exit_game)

                    message0.pack()
                    if temporary == 0:
                        button1.pack()
                    else:
                        button0.pack()

                    win2.mainloop()

                temporary = 1

                if random.randint(0, 9) == 9:
                    random0 = 0
                    temporary = 0
                    if language == 0:
                        txt0 = '这是一伙强盗!很不幸,您的基地被清空了'
                    elif language == 1:
                        txt0 = 'This is a gang of robbers! Unfortunately, your base has been cleared'
                    global vc
                    vc = 3

                    event_refugee_enable(txt0)
                else:
                    random0 = random.randint(5, 30)
                    if language == 0:
                        txt0 = ('您的人口增加了:' + str(random0))
                    elif language == 1:
                        txt0 = ('Your population has increased:' + str(random0))

                    event_refugee_enable(txt0)

            event_win1(txt0, txt1, txt2, event_random1, win1_esc, 1)
        elif random0 == 2:
            if language == 0:
                txt0 = '有一位商人,想和您交易'
                txt1 = '交易'
                txt2 = '赶走'
            elif language == 1:
                txt0 = 'There is a businessman who wants to trade with you'
                txt1 = 'transaction'
                txt2 = 'Drive away'

            def event_random2():
                win2 = Tk()
                win2.title("event_businessman")
                win2.geometry("320x180")
                win2.iconbitmap("1.ico")
                win2.resizable(False, False)

                choice = random.randint(100, 500)

                def event_random2_win2(txt0, txt1, choice):
                    global money
                    money = money + choice

                    def win2_esc():
                        win2.destroy()
                        win1.destroy()

                    message0 = Message(win2, text=txt0, width=300)
                    button0 = Button(win2, text=txt1, command=win2_esc)

                    message0.pack()
                    button0.pack()

                if random.randint(0, 3) == 0:
                    if language == 0:
                        txt0 = '亏了不少:' + str(choice)
                        txt1 = '确定'
                    elif language == 1:
                        txt0 = ('Losing a lot:' + str(choice))
                        txt1 = 'ok'
                    event_random2_win2(txt0, txt1, -choice)
                else:
                    if language == 0:
                        txt0 = ('您的金钱增加了:' + str(choice))
                        txt1 = '确定'
                    elif language == 1:
                        txt0 = ('Your money has increased:' + str(choice))
                        txt1 = 'ok'
                    event_random2_win2(txt0, txt1, choice)

                win2.mainloop()

            event_win1(txt0, txt1, txt2, event_random2, win1_esc, 1)
        elif random0 == 3:
            if random.randint(0, 4) == 4:
                choice = random.randint(100, 500)
                temporary = random.randint(10, 50)

                def event_random3():
                    global field
                    global population
                    field = field - choice
                    population = population - temporary
                    win1.destroy()

                if language == 0:
                    txt0 = '发生了自然灾害,有所损失/n' + '损失土地:' + str(choice) + '/n死亡人口:' + str(temporary)
                    txt1 = '确定'
                elif language == 1:
                    txt0 = ('Natural disasters have occurred and there have been losses/n' + 'Loss of land:' +
                            str(choice) + '/nDeath toll:' + str(temporary))
                    txt1 = 'ok'
                event_win1(txt0, txt1, txt1, event_random3, event_random3, 0)
            else:
                if language == 0:
                    txt0 = '无事发生'
                    txt1 = '确定'
                elif language == 1:
                    txt0 = 'Nothing'
                    txt1 = 'ok'
                event_win1(txt0, txt1, txt1, win1_esc, win1_esc, 0)
        elif random0 == 4:
            choice = random.randint(20, 100)

            def event_random4():
                global field
                global field_current
                print(field)
                field = field + choice
                field_current = field_current + choice
                print(field)
                win1.destroy()

            if language == 0:
                txt0 = ('开垦了一片荒地,增加了不少可用于种植的土地:' + str(choice))
                txt1 = '确定'
            elif language == 1:
                txt0 = ('Reclaimed a piece of wasteland and added a lot of land available for cultivation:' +
                        str(choice))
                txt1 = 'ok'
            event_win1(txt0, txt1, txt1, event_random4, event_random4, 0)


    def next_round():
        win0.destroy()
        global time
        if True:
            global t0
            global vc
            t0 = 1
            if money >= vc_m:
                vc = 0
            elif population >= vc_p:
                vc = 1
            elif food >= vc_f:
                vc = 2
            elif money <= 0:
                vc = 4
            elif population <= 0:
                vc = 5
            else:
                t0 = 0
            time = time + 1


    def view_resources():
        win1 = Tk()
        win1.title("game")
        win1.geometry("320x180")
        win1.iconbitmap("1.ico")
        win1.resizable(False, False)

        if language == 0:
            txt0 = '确定'
            txt1 = ('当前持有金钱:' + str(money))
            txt2 = ('当前持有人口:' + str(population))
            txt3 = ('当前持有食物:' + str(food))
            txt4 = ('当前持有土地:' + str(field))
        elif language == 1:
            txt0 = 'ok'
            txt1 = ('currently holds money:' + str(money))
            txt2 = ('Current population held:' + str(population))
            txt3 = ('Current holdings of food:' + str(food))
            txt4 = ('Currently held land:' + str(field))

        def win1_destroy():
            win1.destroy()

        message0 = Message(win1, text=txt1, width=320)
        message1 = Message(win1, text=txt2, width=320)
        message2 = Message(win1, text=txt3, width=320)
        message3 = Message(win1, text=txt4, width=320)
        button0 = Button(win1, text=txt0, command=win1_destroy)

        message0.pack()
        message1.pack()
        message2.pack()
        message3.pack()
        button0.pack()

        win1.mainloop()


    def store():
        if language == 0:
            txt0 = '购买'
            txt1 = '人口'
            txt2 = '土地'
            txt3 = '返回'
        elif language == 1:
            txt0 = 'buy'
            txt1 = 'population'
            txt2 = 'field'
            txt3 = 'return'

        win1 = Tk()
        win1.title("store")
        win1.geometry("320x180")
        win1.iconbitmap("1.ico")
        win1.resizable(False, False)

        def store_population():
            win2 = Tk()
            win2.title("store_population")
            win2.geometry("320x180")
            win2.iconbitmap("1.ico")
            win2.resizable(False, False)

            temporary = money // population_price

            if language == 0:
                txt0 = '您现在可以买' + str(temporary) + '人'
                txt1 = '确定'
                txt2 = '返回'
                txt3 = '当前人口价格(1x):' + str(population_price)
                txt4 = '清空'
            elif language == 1:
                txt0 = 'You can buy ' + str(temporary) + ' people now'
                txt1 = 'ok'
                txt2 = 'return'
                txt3 = 'Current population prices(1x):' + str(population_price)
                txt4 = 'empty'

            def store_population_ok():
                if language == 0:
                    txt0 = '请输入有效的值'
                    txt1 = '超出可购买范围'
                elif language == 1:
                    txt0 = 'Please enter a valid value'
                    txt1 = 'Beyond the purchasing range'

                if str.isdigit(entry0.get()):
                    if int(entry0.get()) > temporary or int(entry0.get()) <= 0:
                        store_population_entry_delete()
                        messagebox.showinfo("!", txt1)
                    else:
                        global money
                        global population
                        global population_price
                        population += int(entry0.get())
                        money -= int(entry0.get()) * population_price
                        population_price = population_price * 1.05
                        population_price = population_price // 1 + 1
                        store_population_return()

                else:
                    store_population_entry_delete()
                    messagebox.showinfo("!", txt0)

            def store_population_entry_delete():
                entry0.delete(0, 'end')

            def store_population_return():
                win2.destroy()

            message0 = Message(win2, text=txt0, width=320)
            message1 = Message(win2, text=txt3, width=320)
            entry0 = Entry(win2)
            button0 = Button(win2, text=txt1, command=store_population_ok)
            button1 = Button(win2, text=txt4, command=store_population_entry_delete)
            button2 = Button(win2, text=txt2, command=store_population_return)

            message0.pack()
            message1.pack()
            entry0.pack()
            button0.pack()
            button1.pack()
            button2.pack()

            win2.mainloop()

        def store_field():

            win2 = Tk()
            win2.title("store_field")
            win2.geometry("320x180")
            win2.iconbitmap("1.ico")
            win2.resizable(False, False)

            temporary = money // field_price

            if language == 0:
                txt0 = '您现在可以买' + str(temporary) + '人'
                txt1 = '确定'
                txt2 = '返回'
                txt3 = '当前土地价格(1x):' + str(field_price)
                txt4 = '清空'
            elif language == 1:
                txt0 = 'You can buy ' + str(temporary) + ' people now'
                txt1 = 'ok'
                txt2 = 'return'
                txt3 = 'Current field prices(1x):' + str(field_price)
                txt4 = 'empty'

            def store_field_ok():
                if language == 0:
                    txt0 = '请输入有效的值'
                    txt1 = '超出可购买范围'
                elif language == 1:
                    txt0 = 'Please enter a valid value'
                    txt1 = 'Beyond the purchasing range'

                if str.isdigit(entry0.get()):
                    if int(entry0.get()) > temporary or int(entry0.get()) <= 0:
                        store_field_entry_delete()
                        messagebox.showinfo("!", txt1)
                    else:
                        global money
                        global field
                        global field_price
                        field += int(entry0.get())
                        money -= int(entry0.get()) * field_price
                        field_price = field_price * 1.05
                        field_price = field_price // 1 + 1
                        store_field_return()

                else:
                    store_field_entry_delete()
                    messagebox.showinfo("!", txt0)

            def store_field_entry_delete():
                entry0.delete(0, 'end')

            def store_field_return():
                win2.destroy()

            message0 = Message(win2, text=txt0, width=320)
            message1 = Message(win2, text=txt3, width=320)
            entry0 = Entry(win2)
            button0 = Button(win2, text=txt1, command=store_field_ok)
            button1 = Button(win2, text=txt4, command=store_field_entry_delete)
            button2 = Button(win2, text=txt2, command=store_field_return)

            message0.pack()
            message1.pack()
            entry0.pack()
            button0.pack()
            button1.pack()
            button2.pack()

            win2.mainloop()

        def store_return():
            win1.destroy()

        message0 = Message(win1, text=txt0, width=320)
        button0 = Button(win1, text=txt1, command=store_population)
        button1 = Button(win1, text=txt2, command=store_field)
        button2 = Button(win1, text=txt3, command=store_return)

        message0.pack()
        button0.pack()
        button1.pack()
        button2.pack()

        win1.mainloop()


    if event == 1:
        event_enable()
    elif not event == 9:
        if language == 0:
            txt9 = '事件未启用'
        elif language == 1:
            txt9 = 'Event not enabled'
        messagebox.showerror('event_not', txt9)
        event = 9

    button0 = Button(win0, text=txt0, command=esc)
    button1 = Button(win0, text=txt1, command=next_round)
    button2 = Button(win0, text=txt2, command=view_resources)
    button3 = Button(win0, text=txt3, command=store)

    button2.pack()
    button3.pack()
    button1.pack()
    button0.pack()

    win0.mainloop()
#  结束页
if True:
    win0 = Tk()
    win0.title("trailer page")
    win0.geometry("320x180")
    win0.iconbitmap("1.ico")
    win0.resizable(False, False)

    txt = open('user.txt', 'w')
    txt.write('version;' + str(version) + ';user;' + str(user) + ';time;' + str(time) + ';Victory conditions;' +
              str(vc))
    txt.close()

    vc_vc(vc)

    if language == 0:
        txt0 = ('感谢您的游玩:' + user)
        txt1 = ('游戏总用时:' + str(time))
        txt2 = (temporary[0])
        txt3 = '确定'
    elif language == 1:
        txt0 = ('Thank you for play:' + user)
        txt1 = ('Total game time:' + str(time))
        txt2 = (temporary[1])
        txt3 = 'ok'

    message0 = Message(win0, text=txt0, width=300)
    message1 = Message(win0, text=txt1, width=300)
    message2 = Message(win0, text=txt2, width=300)
    button0 = Button(win0, text=txt3, command=esc)

    message0.pack()
    message1.pack()
    message2.pack()
    button0.pack()

    win0.mainloop()
