#  Copyright (c)

# 回合制生存游戏
# 开始时间2024-04-04
# 单人开发(702361946@qq.com)
# 版权所有，拒绝盗用
import os

print('702361946@qq.com')
# 默认调用值
if True:
    import random

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
    if language == 0:
        print('zh')
    elif language == 1:
        print('en')
    if not verification == '0':
        print('Please check resource integrity.')
        print('请检查资源完整性。')
        input('Enter')
        os.abort()

# 开始前模块(user+记录+修改器)
while t0 < 1:
    if language == 0:
        choice = input('''查看上一次游戏记录或开启新游戏
0 上一次的记录
1 新游戏
2 设置
3 退出游戏''')
    elif language == 1:
        choice = input('''View previous game records or start a new game
0 Last Record
1 New game
2 Settings
3 exit the game''')
    if choice == '0':
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
            print('上一次的版本:' + version_Last)
            print('上一次的用户名:' + user)
            print('上一次游戏总用时:' + time)
            print(temporary[0])
        elif language == 1:
            print('Last version:' + version_Last)
            print('Last username:' + user)
            print('Last game total time:' + time)
            print(temporary[1])
    elif choice == '1':
        t0 = 1
        if language == 0:
            print('加载...')
        elif language == 1:
            print('loading...')
    elif choice == '2':
        t1 = 0
        while t1 < 1:
            if language == 0:
                choice = input('''0 语言
1 修改器
2 返回上一级''')
            elif language == 1:
                choice = input('''0 Language
1 modifier
2 Return to the previous level''')
            if choice == '0':
                t2 = 0
                while t2 < 1:
                    t2 = 1
                    print('''0 Chinese
1 English''')
                    if language == 0:
                        choice = input('2 上一级')
                    elif language == 1:
                        choice = input('2 Previous level')
                    if choice == '0':
                        language = 0
                        print('完成')
                    elif choice == '1':
                        language = 1
                        print('complete')
                    elif choice == '2':
                        if language == 0:
                            print('上一级')
                        elif language == 1:
                            print('Previous level')
                    else:
                        if language == 0:
                            print('请输入有效的值')
                        elif language == 1:
                            print('Please enter a valid value')
                            t2 = 1
                    txt = open('version.txt', 'w')
                    txt.write(
                        version + ';' + str(money) + ';' + str(population) + ';' + str(
                            population_price) + ';' + str(
                            food) + ';' + str(field) + ';' + str(field_min) + ';' + str(field_max) + ';' + str(
                            field_price) + ';' + str(vc_m) + ';' + str(vc_p) + ';' + str(vc_f_m) + ';' + str(
                            language) + ';' + str(verification))
                    txt.close()
            elif choice == '1':
                t2 = 0
                while t2 < 1:
                    t3 = 0
                    if language == 0:
                        choice = input('''修改目标或资源
0 金钱
1 人口
2 食物
3 土地
4 事件
5 退出修改器''')
                    elif language == 1:
                        choice = input('''Modifying goals or resources
0 money
1 population
2 food
3 field
4 event
5 exit modifier''')
                    if choice == '0':
                        while t3 < 1:
                            if language == 0:
                                choice = input('''0 当前持有金钱
1 金钱胜利目标
2 上一级''')
                            elif language == 1:
                                choice = input('''0 currently holds money
1 Money Victory Goal
2 Previous level''')
                            if choice == '0':
                                if language == 0:
                                    print('当前持有金钱:' + str(money))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('currently holds money：' + str(money))
                                    choice = input('Enter a new value (must be an integer)')
                                money = int(choice)
                            elif choice == '1':
                                if language == 0:
                                    print('当前金钱胜利目标:' + str(vc_m))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current Money Victory Goal：' + str(vc_m))
                                    choice = input('Enter a new value (must be an integer)')
                                vc_m = int(choice)
                            elif choice == '2':
                                t3 = 1
                    elif choice == '1':
                        while t3 < 1:
                            if language == 0:
                                choice = input('''0 当前持有人口
1 人口胜利目标
2 上一级''')
                            elif language == 1:
                                choice = input('''0 Current population held
1 Population Victory Goal
2 Previous level''')
                            if choice == '0':
                                if language == 0:
                                    print('当前持有人口:' + str(population))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current population held：' + str(population))
                                    choice = input('Enter a new value (must be an integer)')
                                population = int(choice)
                            elif choice == '1':
                                if language == 0:
                                    print('当前人口胜利目标:' + str(vc_p))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current population victory target：' + str(vc_p))
                                    choice = input('Enter a new value (must be an integer)')
                                vc_p = int(choice)
                            elif choice == '2':
                                t3 = 1
                    elif choice == '2':
                        while t3 < 1:
                            if language == 0:
                                choice = input('''0 当前持有食物
1 食物胜利目标
2 上一级''')
                            elif language == 1:
                                choice = input('''0 Current holdings of food
1 Food Victory Goal
2 Previous level''')
                            if choice == '0':
                                if language == 0:
                                    print('当前持有食物:' + str(food))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current holdings of food：' + str(food))
                                    choice = input('Enter a new value (must be an integer)')
                                food = int(choice)
                            elif choice == '1':
                                if language == 0:
                                    print('当前食物胜利目标(人口倍率):' + str(vc_f_m))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current food victory target (population multiplier)：' + str(vc_f_m))
                                    choice = input('Enter a new value (must be an integer)')
                                vc_f_m = int(choice)
                            elif choice == '2':
                                t3 = 1
                    elif choice == '3':
                        while t3 < 1:
                            if language == 0:
                                choice = input('''0 当前持有土地
1 当前土地上限
2 抽取土地下限
3 抽取土地上限
4 土地初始价格
5 上一级''')
                            elif language == 1:
                                choice = input('''0 Currently held land
1 Current Land Cap
2 Extract the lower limit of land
3 Upper limit of land extraction
4 Initial land price
5 Previous level''')
                            if choice == '0':
                                if language == 0:
                                    print('当前持有土地:' + str(field))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current land holdings：' + str(field))
                                    choice = input('Enter a new value (must be an integer)')
                                field = int(choice)
                            elif choice == '1':
                                if language == 0:
                                    print('当前土地上限:' + str(field_current))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current land cap：' + str(field_current))
                                    choice = input('Enter a new value (must be an integer)')
                                field_current = int(choice)
                            elif choice == '2':
                                if language == 0:
                                    print('当前抽取土地下限:' + str(field_min))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('The current lower limit of land extraction：' + str(field_min))
                                    choice = input('Enter a new value (must be an integer)')
                                field_min = int(choice)
                            elif choice == '3':
                                if language == 0:
                                    print('当前抽取土地上限:' + str(field_max))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Current land extraction limit：' + str(field_max))
                                    choice = input('Enter a new value (must be an integer)')
                                field_max = int(choice)
                            elif choice == '4':
                                if language == 0:
                                    print('初始土地价格:' + str(field_price))
                                    choice = input('输入新的值(需为整数)')
                                elif language == 1:
                                    print('Initial land price：' + str(field_price))
                                    choice = input('Enter a new value (must be an integer)')
                                field_price = int(choice)
                            elif choice == '5':
                                t3 = 1
                    elif choice == '4':
                        if language == 0:
                            choice = input('''0 关闭
1 开启''')
                        elif language == 1:
                            choice = input('''0 Close
1 Open''')
                        event = int(choice)
                        txt = open('event.txt', 'w')
                        txt.write(' ;' + str(event))
                        txt.close()
                    elif choice == '5':
                        t2 = 1
                    txt = open('version.txt', 'w')
                    txt.write(
                        version + ';' + str(money) + ';' + str(population) + ';' + str(
                            population_price) + ';' + str(
                            food) + ';' + str(field) + ';' + str(field_min) + ';' + str(field_max) + ';' + str(
                            field_price) + ';' + str(vc_m) + ';' + str(vc_p) + ';' + str(vc_f_m) + ';' + str(
                            language) + ';' + str(verification))
                    txt.close()
                    if language == 0:
                        print('重启游戏生效')
                        print()
                    elif language == 1:
                        print('Restarting the game takes effect')
                        print()
            elif choice == '2':
                t1 = 1
                if language == 0:
                    print('上一级')
                elif language == 1:
                    print('Previous level')
            else:
                if language == 0:
                    print('请输入有效的值')
                elif language == 1:
                    print('Please enter a valid value')
    elif choice == '3':
        os.abort()
    else:
        if language == 0:
            print('请输入有效的值')
        elif language == 1:
            print('Please enter a valid value')

# 主模块重定义
if True:
    t0 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    if language == 0:
        print('完成')
    elif language == 1:
        print('complete')

# hello and user
if True:
    while t0 < 1:
        if language == 0:
            choice = input('''0 复用上一次的用户名
1 新的用户名''')
        elif language == 1:
            choice = input('''0 Reuse the previous username
1 New username''')
        if choice == '0':
            t0 = 1
        elif choice == '1':
            t1 = 0
            while t1 < 1:
                t1 = 1
                if language == 0:
                    temporary = input('如何称呼您?')
                elif language == 1:
                    temporary = input('How do I address you?')
                t2 = 0
                while t2 < 1:
                    t2 = 1
                    if language == 0:
                        choice = input('确定?(回答yes或者no)')
                    elif language == 1:
                        choice = input('Are you sure?(yes or no)')
                    if choice == 'yes':
                        user = temporary
                        t0 = 1
                    elif choice == 'no':
                        t1 = 0
                    else:
                        t2 = 0
                        if language == 0:
                            print('请输入有效的值')
                        elif language == 1:
                            print('Please enter a valid value')
        else:
            if language == 0:
                print('请输入有效的值')
            elif language == 1:
                print('Please enter a valid value')

    txt = open('user.txt', 'w')
    txt.write('version;' + str(version) + ';user;' + str(user) + ';time;' + str(time) + ';Victory conditions;' +
              str(vc))
    txt.close()
    if language == 0:
        print('欢迎:' + user)
    elif language == 1:
        print('hello:' + user)

# 主模块重定义
if True:
    t0 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0

    time = 0

# 主游戏模块
if True:
    while t0 < 1:
        t1 = 0
        time = time + 1
        if language == 0:
            print('当前回合:' + str(time))
        elif language == 1:
            print('Current round:' + str(time))
        # 事件
        if event == 1:
            t3 = 0
            while t3 < 1:
                t3 = 1
                choice = random.randint(0, 4)
                if choice == 0:
                    if language == 0:
                        print('无事')
                    elif language == 1:
                        print('Nothing')
                # 难民
                elif choice == 1:
                    if language == 0:
                        choice = input('''有一群难民,请求您的收留
0 收留
1 赶走''')
                    elif language == 1:
                        choice = input('''There is a group of refugees requesting your accommodation
0 retention
1 Drive away''')
                    if choice == '0':
                        choice = random.randint(0, 9)
                        if choice == 9:
                            if language == 0:
                                print('这是一伙强盗!很不幸,您的基地被清空了')
                            elif language == 1:
                                print('This is a gang of robbers! Unfortunately, your base has been cleared')
                            vc = 3
                            t0 = 1
                            t1 = 1
                            t2 = 1
                            t3 = 1
                        else:
                            choice = random.randint(5, 20)
                            population = population + choice
                            if language == 0:
                                print('您的人口增加了:' + str(choice))
                            elif language == 1:
                                print('Your population has increased:' + str(choice))
                    else:
                        if language == 0:
                            print('赶走了')
                        elif language == 1:
                            print('Drive away')
                # 商人
                elif choice == 2:
                    if language == 0:
                        choice = input('''有一位商人,想和您交易
0 交易
1 赶走''')
                    elif language == 1:
                        choice = input('''There is a businessman who wants to trade with you
0 transaction
1 Drive away''')
                    if choice == '0':
                        choice = random.randint(0, 2)
                        if choice == 2:
                            choice = random.randint(100, 500)
                            money = money - choice
                            if language == 0:
                                print('亏了不少:' + str(choice))
                            elif language == 1:
                                print('Losing a lot:' + str(choice))
                        else:
                            choice = random.randint(100, 500)
                            money = money + choice
                            if language == 0:
                                print('您的金钱增加了:' + str(choice))
                            elif language == 1:
                                print('Your money has increased:' + str(choice))
                    else:
                        if language == 0:
                            print('赶走了')
                        elif language == 1:
                            print('Drive away')
                # 天灾
                elif choice == 3:
                    choice = random.randint(0, 4)
                    if choice == 4:
                        choice = random.randint(100, 500)
                        temporary = random.randint(10, 50)
                        field = field - choice
                        population = population - temporary
                        if language == 0:
                            print('发生了自然灾害,有所损失')
                            print('损失土地:' + str(choice))
                            print('死亡人口:' + str(temporary))
                        elif language == 1:
                            print('Natural disasters have occurred and there have been losses')
                            print('Loss of land:' + str(choice))
                            print('Death toll:' + str(temporary))
                    else:
                        if language == 0:
                            print('无事')
                        elif language == 1:
                            print('Nothing')
                # 开垦荒地
                elif choice == 4:
                    choice = random.randint(20, 100)
                    field = field + choice
                    field_current = field_current + choice
                    if language == 0:
                        print('开垦了一片荒地,增加了不少可用于种植的土地:' + str(choice))
                    elif language == 1:
                        print('Reclaimed a piece of wasteland and added a lot of land available for cultivation:' +
                              str(choice))
        else:
            if language == 0:
                print('事件未启用')
            elif language == 1:
                print('Event not enabled')
        # 游戏
        while t1 < 1:
            # 资源查看 and 购买 and 下一回合
            if True:
                if language == 0:
                    choice = input('''0 查看资源
1 商店
2 下一回合
9 结束游戏''')
                elif language == 1:
                    choice = input('''0 View Resources
1 Store
2 Next round
9 End the game''')
                if choice == '0':
                    if language == 0:
                        print('当前持有金钱:' + str(money))
                        print('当前持有人口:' + str(population))
                        print('当前持有食物:' + str(food))
                        print('当前持有土地:' + str(field))
                    elif language == 1:
                        print('currently holds money:' + str(money))
                        print('Current population held:' + str(population))
                        print('Current holdings of food:' + str(food))
                        print('Currently held land:' + str(field))
                elif choice == '1':
                    t2 = 0
                    while t2 < 1:
                        t3 = 0
                        if language == 0:
                            choice = input('''0 人口
1 土地
2 退出商店''')
                        elif language == 1:
                            choice = input('''0 population
1 Land
2 exit the store''')
                        if choice == '0':
                            while t3 < 1:
                                if language == 0:
                                    print('当前人口价格(1x):' + str(population_price))
                                    choice = input('''0 购买
1 上一级''')
                                elif language == 1:
                                    print('Current population prices(1x):' + str(population_price))
                                    choice = input('''0 buy?
1 Previous level''')
                                if choice == '0':
                                    if language == 0:
                                        choice = input('''输入购买的数量(需为整数)''')
                                        txt0 = '不能小于等于0!'
                                    elif language == 1:
                                        choice = input('''Enter the quantity purchased (must be an integer)''')
                                        txt0 = 'Cannot be less than or equal to 0!'
                                    if int(choice) * population_price > money:
                                        if language == 0:
                                            print('请至少准备金钱:' + str(int(choice) * population_price))
                                        elif language == 1:
                                            print('Please prepare at least money:' +
                                                  str(int(choice) * population_price))
                                    elif int(choice) <= 0:
                                        print(txt0)
                                        print()
                                    elif int(choice) * population_price <= money:
                                        if language == 0:
                                            print('购买成功')
                                        elif language == 1:
                                            print('Purchase successful')
                                        money = money - int(choice) * population_price
                                        population = population + int(choice)
                                        population_price = population_price * 1.1
                                    else:
                                        if language == 0:
                                            print('请输入有效的值')
                                        elif language == 1:
                                            print('Please enter a valid value')
                                elif choice == '1':
                                    t3 = 1
                                else:
                                    if language == 0:
                                        print('请输入有效的值')
                                    elif language == 1:
                                        print('Please enter a valid value')
                        elif choice == '1':
                            while t3 < 1:
                                if language == 0:
                                    print('当前土地价格(1x):' + str(field_price))
                                    choice = input('''0 购买
1 上一级''')
                                elif language == 1:
                                    print('Current land prices(1x):' + str(field_price))
                                    choice = input('''0 buy?
1 Previous level''')
                                if choice == '0':
                                    if language == 0:
                                        choice = input('''输入购买的数量(需为整数)''')
                                        txt0 = '不能小于等于0!'
                                    elif language == 1:
                                        choice = input('''Enter the quantity purchased (must be an integer)''')
                                        txt0 = 'Cannot be less than or equal to 0!'
                                    if int(choice) * field_price > money:
                                        if language == 0:
                                            print('请至少准备金钱:' + str(int(choice) * field_price))
                                        elif language == 1:
                                            print('Please prepare at least money:' + str(int(choice) * field_price))
                                    elif int(choice) <= 0:
                                        print(txt0)
                                        print()
                                    elif int(choice) * field_price <= money:
                                        if language == 0:
                                            print('购买成功')
                                        elif language == 1:
                                            print('Purchase successful')
                                        money = money - int(choice) * field_price
                                        field = field + int(choice)
                                        field_price = field_price * 1.2
                                    else:
                                        if language == 0:
                                            print('请输入有效的值')
                                        elif language == 1:
                                            print('Please enter a valid value')
                                elif choice == '1':
                                    t3 = 1
                                else:
                                    if language == 0:
                                        print('请输入有效的值')
                                    elif language == 1:
                                        print('Please enter a valid value')
                        elif choice == '2':
                            t2 = 1
                        else:
                            if language == 0:
                                print('请输入有效的值')
                            elif language == 1:
                                print('Please enter a valid value')
                elif choice == '2':
                    if food + field < population:
                        population = food + field
                        food = 0
                        if language == 0:
                            print('食物不足')
                        elif language == 1:
                            print('Lack of food')
                    else:
                        food = food + field - population
                    money = money + population - field
                    t1 = 1
                elif choice == '9':
                    if language == 0:
                        choice = input('确定?(yes or no)')
                    elif language == 1:
                        choice = input('Are you sure?(yes or no)')
                    if choice == 'yes':
                        print('exit')
                        os.abort()
                else:
                    if language == 0:
                        print('请输入有效的值')
                    elif language == 1:
                        print('Please enter a valid value')

        # 游戏结束判定
        if True:
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

# 结束以及记录
if True:
    if language == 0:
        print('游戏结束了')
        print('感谢您的游玩')
    elif language == 1:
        print('The game is over')
        print('Thank you for play')
    if choice == '0':
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
            print('游戏总用时:' + time)
            print(temporary[0])
        elif language == 1:
            print('Total game time:' + time)
            print(temporary[1])

# 记录
if True:
    txt = open('user.txt', 'w')
    txt.write('version;' + str(version) + ';user;' + str(user) + ';time;' + str(time) + ';Victory conditions;' +
              str(vc))
    txt.close()
    os.abort()
