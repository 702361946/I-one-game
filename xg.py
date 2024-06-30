import os

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

t0 = 0
while t0 < 1:
    t1 = 0
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
        while t1 < 1:
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
                t1 = 1
    elif choice == '1':
        while t1 < 1:
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
                t1 = 1
    elif choice == '2':
        while t1 < 1:
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
                t1 = 1
    elif choice == '3':
        while t1 < 1:
            if language == 0:
                choice = input('''0 当前持有土地
1 抽取土地下限
2 抽取土地上限
3 土地初始价格
4 上一级''')
            elif language == 1:
                choice = input('''0 Currently held land
1 Extract the lower limit of land
2 Upper limit of land extraction
3 Initial land price
4 Previous level''')
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
                    print('当前抽取土地下限:' + str(field_min))
                    choice = input('输入新的值(需为整数)')
                elif language == 1:
                    print('The current lower limit of land extraction：' + str(field_min))
                    choice = input('Enter a new value (must be an integer)')
                field_min = int(choice)
            elif choice == '2':
                if language == 0:
                    print('当前抽取土地上限:' + str(field_max))
                    choice = input('输入新的值(需为整数)')
                elif language == 1:
                    print('Current land extraction limit：' + str(field_max))
                    choice = input('Enter a new value (must be an integer)')
                field_max = int(choice)
            elif choice == '3':
                if language == 0:
                    print('初始土地价格:' + str(field_price))
                    choice = input('输入新的值(需为整数)')
                elif language == 1:
                    print('Initial land price：' + str(field_price))
                    choice = input('Enter a new value (must be an integer)')
                field_price = int(choice)
            elif choice == '4':
                t1 = 1
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
        t0 = 1
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
        input('按下回车继续')
    elif language == 1:
        print('Restarting the game takes effect')
        print()
        input('Press enter to continue')
    os.abort()
