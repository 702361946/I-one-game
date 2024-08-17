#  Copyright (c)

import json

version_string = {
    'money': 1000,
    'population': 100,
    'food': 100,
    'field': 100,
    'field_max': 5000,
    'price_population': 10,
    'price_field': 10,
    'Victory conditions_money': 10000,
    'Victory conditions_population': 1000,
    'Victory conditions_food_Multiplier': 1000
}


# 使用json.dump()将字典写入到文件中
def sys_w_version_json():
    with open('sys_version.json', 'w') as f:
        json.dump(version_string, f, indent=4)


# 使用json.dump()将字典写入到文件中
def user_w_version_json():
    with open('user_version.json', 'w') as f:
        json.dump(version_string, f, indent=4)
