#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------
#  Name:        oneweather1.py
#  Created:     15-12-16 pocmon
#  Edition:     Python3.4, pychrom
#  License:     MIT <http://opensource.org/licenses/MIT>
#  Copyright:   (c) pocmon <pocmon@sina.com>
#--------------------------------------------------------
#  **Note:
#  新功能：存储查询城市到配置文件，不带参数默认为从配置文件读取上
#  次正确的查询城市。
#  **Warning: ...
#--------------------------------------------------------
#


import json
import urllib.request
import urllib.parse
import gzip
import sys
import os
import unicodedata

# 默认城市
city = '深圳'
# 配置文件HOME路径
home = os.environ['HOME']
# 判断汉字条件
chz = True
phz = True


# 读取配置文件中城市名称，返回city
def read_conf():
    if (os.path.exists('%s/.oneweather' % (home))) and (os.path.isfile('%s/.oneweather/location.json' % (home))):
        f = open('%s/.oneweather/location.json' % (home), 'r')
        line = f.readline()

        try:
            conf = json.loads(line)
            f.close()
            hzcc = conf['city']

            # JSON文件中城市名数据错误
            if if_hz(hzcc):
                return conf['city']
            else:
                print('\n\033[1;31;0m配置文件中城市格式错误，%s/.oneweather/location.json\033[0m' % (home))

        # 非JSON格式文件
        except:
            print('\n\033[1;31;0m配置文件格式错误，%s/.oneweather/location.json\033[0m' % (home))

    return city


# 保存城市名称
def save_conf(city):
    if not (os.path.exists('%s/.oneweather' % (home))):
        os.mkdir('%s/.oneweather' % (home))

    f = open('%s/.oneweather/location.json' % (home), 'w')
    conf = '{\"city\": \"%s\"}' % (city)
    f.write(conf)
    f.close()


# 判断参数是否为汉字串，是汉字串True
def if_hz(hzcc):
    phz = True
    for cs in range(0, len(hzcc)):

        if unicodedata.east_asian_width(hzcc[cs]) != 'Na':
            chz = True
        else:
            chz = False

        phz = (chz and phz)

    return phz


# 显示天气信息
def winfo(city):

    print("\n城市：" + city + "\n")

    # 网址中汉字处理，城市名称
    city = urllib.parse.quote(city)

    # 获取JSON
    url = "http://wthrcdn.etouch.cn/weather_mini?city=%s" % (city)
    mys = urllib.request.urlopen(url).read()
    # 解压JSON，并转码
    myw = gzip.decompress(mys).decode('utf-8')

    myj = json.loads(myw)

    if myj["desc"] == "OK":
        city = myj["data"]["city"]
        wendu = myj["data"]["wendu"]
        weather = myj["data"]["ganmao"]

        save_conf(city)

        print("\033[1;33;0m" + "实时天气：" + "\033[0m")
        print("\t" + (wendu + "℃ ").ljust(5) + weather + "\n")

        print("\033[1;33;0m" + "今日天气：" + "\033[0m")
        high = myj["data"]["forecast"][0]["high"]  # 最高温度
        fengxiang = myj["data"]["forecast"][0]["fengxiang"]  # 风向
        fengli = myj["data"]["forecast"][0]["fengli"]  # 风力
        type = myj["data"]["forecast"][0]["type"]  # 天气类型
        low = myj["data"]["forecast"][0]["low"]  # 最低温度
        date = myj["data"]["forecast"][0]["date"]  # 日期
        print("\t" + date + type.center(10) + "\t" + high.ljust(10) + low.ljust(10) + fengli + "\t" + fengxiang)

        print("\033[1;33;0m" + "\n未来四天预报：" + "\033[0m")
        for wday in range(1, 5):
            high = myj["data"]["forecast"][wday]["high"]  # 最高温度
            fengxiang = myj["data"]["forecast"][wday]["fengxiang"]  # 风向
            fengli = myj["data"]["forecast"][wday]["fengli"]  # 风力
            type = myj["data"]["forecast"][wday]["type"]  # 天气类型
            low = myj["data"]["forecast"][wday]["low"]  # 最低温度
            date = myj["data"]["forecast"][wday]["date"]  # 日期
            print("\t" + date + type.center(10) + "\t" + high.ljust(10) + low.ljust(10) + fengli + "\t" + fengxiang)

        print("\033[1;33;0m" + "\n昨日天气：" + "\033[0m")
        high = myj["data"]["yesterday"]["high"]  # 最高温度
        fengxiang = myj["data"]["yesterday"]["fx"]  # 风向
        fengli = myj["data"]["yesterday"]["fl"]  # 风力
        type = myj["data"]["yesterday"]["type"]  # 天气类型
        low = myj["data"]["yesterday"]["low"]  # 最低温度
        date = myj["data"]["yesterday"]["date"]  # 日期
        print("\t" + date + type.center(10) + "\t" + high.ljust(10) + low.ljust(10) + fengli + "\t" + fengxiang)

    else:
        print("要查询的城市未找到，请检查城市名称是否正确！本程序只支持中国城市名称！")


def main():
    # 参数超过2个，命令格式错误
    if len(sys.argv) > 2:
        print("\n请输入正确的命令：oneweathert.py [中国城市名称]，目前本程序只支持一个城市的天气询查！")
        print("如：oneweathert.py 北京 , 不带城市名称，默认上次城市")

    # 没有参数就从配置文件读取上次查询的城市，如果没有配置文件，则使用程序默认城市：深圳
    elif len(sys.argv) == 1:
        city = read_conf()
        print("\n可输入城市名参数：oneweathert.py [中国城市名称],如：oneweathert.py 北京 , 不带城市名称，默认上次城市")
        winfo(city)

    elif len(sys.argv) == 2:

        # 判断参数是否为汉字，只支持汉字
        hzcc = sys.argv[1]
        if not if_hz(hzcc):
            print("\n请检查城市名称是否正确，本程序只支持中国中文城市名称！")
        else:
            city = sys.argv[1]
            winfo(city)


# start...
if __name__ == '__main__':
    main()
