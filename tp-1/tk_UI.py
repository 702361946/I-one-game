# -*- coding: UTF-8 -*-
#  赋值
if True:
    import random
    import os
    from tkinter import *

    t0 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0

    choice = 0

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

    def glo_bal():
        global version
        global money
        global population
        global population_price
        global food
        global field
        global field_min
        global field_max
        global field_price
        global vc_m
        global vc_p
        global vc_f_m
        global language
        global verification

    glo_bal()
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
        exit()


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

                exit()

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
#  主游戏
if True:
    time = 0

    win0 = Tk()
    win0.title("game")
    win0.geometry("320x180")
    win0.iconbitmap("1.ico")
    win0.resizable(False, False)


    def event_enable():
        win1 = Tk()
        win1.title("event")
        win1.geometry("320x180")
        win1.iconbitmap("1.ico")
        win1.resizable(False, False)

        def win1_esc():
            win1.destroy()

        def event_win1(txt0, txt1, txt2, button0_def, button1_def):
            message0 = Message(win1, text=txt0, width=300)
            button0 = Button(win1, text=txt1, command=button0_def)
            button1 = Button(win1, text=txt2, command=button1_def)

            message0.pack()
            button0.pack()
            if temporary == 1:
                button1.pack()

        random.randint(0, 4)
        random0 = 1
        if random0 == 0:
            temporary = 0
            if language == 0:
                txt0 = '无事发生'
                txt1 = '确定'
            elif language == 1:
                txt0 = 'Nothing'
                txt1 = 'ok'

            event_win1(txt0, txt1, txt1, win1_esc, win1_esc)
        elif random0 == 1:
            temporary = 1
            if language == 0:
                txt0 = '有一群难民,请求您的收留'
                txt1 = '收留'
                txt2 = '赶走'
            elif language == 1:
                txt0 = 'There is a group of refugees requesting your accommodation'
                txt1 = 'retention'
                txt2 = 'Drive away'

            def event_refugee():
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

            event_win1(txt0, txt1, txt2, event_refugee, win1_esc)
        elif random0 == 2:
            print()
        elif random0 == 3:
            print()
        elif random0 == 4:
            print()


    if event == 1:
        event_enable()

    button0 = Button(win0, text=txt0, command=esc)

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

    if vc == '0':
        temporary = ['胜利方式:金钱', 'Victory method:money']
    elif vc == '1':
        temporary = ['胜利方式:人口', 'Victory method:population']
    elif vc == '2':
        temporary = ['胜利方式:食物', 'Victory method:food']
    elif vc == '3':
        temporary = ['失败方式:被强盗杀死', 'Failure mode:Killed by bandits']
    elif vc == '4':
        temporary = ['失败方式:破产', 'Failure mode:bankruptcy']
    elif vc == '5':
        temporary = ['失败方式:集体死亡', 'Failure mode:Collective death']
    else:
        temporary = ['?', '?']

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
