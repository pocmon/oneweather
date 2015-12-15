#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  oneweather.py v1.03 不可保存查询城市名称，不带配置文件版本
#
#  Copyright 2015 pocmon <pocmon@sina.com> MIT License
#

import json
import urllib.request
import urllib.parse
import gzip
import sys
import unicodedata

# 默认城市
city = '深圳'
# 判断汉字条件
chz = True
phz = True


def winfo(city):  # 显示天气信息

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

        print("\033[5;33;0m" + "实时天气：" + "\033[0m")
        print("\t" + (wendu + "℃ ").ljust(5) + weather + "\n")

        print("\033[5;33;0m" + "今日天气：" + "\033[0m")
        high = myj["data"]["forecast"][0]["high"]  # 最高温度
        fengxiang = myj["data"]["forecast"][0]["fengxiang"]  # 风向
        fengli = myj["data"]["forecast"][0]["fengli"]  # 风力
        type = myj["data"]["forecast"][0]["type"]  # 天气类型
        low = myj["data"]["forecast"][0]["low"]  # 最低温度
        date = myj["data"]["forecast"][0]["date"]  # 日期
        print("\t" + date + "\t" + type + "\t" + high.ljust(10) + low.ljust(10) + fengli + "\t" + fengxiang)

        print("\033[5;33;0m" + "\n未来四天预报：" + "\033[0m")
        for wday in range(1, 5):
            high = myj["data"]["forecast"][wday]["high"]  # 最高温度
            fengxiang = myj["data"]["forecast"][wday]["fengxiang"]  # 风向
            fengli = myj["data"]["forecast"][wday]["fengli"]  # 风力
            type = myj["data"]["forecast"][wday]["type"]  # 天气类型
            low = myj["data"]["forecast"][wday]["low"]  # 最低温度
            date = myj["data"]["forecast"][wday]["date"]  # 日期
            print("\t" + date + type.center(10) + "\t" + high.ljust(10) + low.ljust(10) + fengli + "\t" + fengxiang)

        print("\033[5;33;0m" + "\n昨日天气：" + "\033[0m")
        high = myj["data"]["yesterday"]["high"]  # 最高温度
        fengxiang = myj["data"]["yesterday"]["fx"]  # 风向
        fengli = myj["data"]["yesterday"]["fl"]  # 风力
        type = myj["data"]["yesterday"]["type"]  # 天气类型
        low = myj["data"]["yesterday"]["low"]  # 最低温度
        date = myj["data"]["yesterday"]["date"]  # 日期
        print("\t" + date + "\t" + type + "\t" + high.ljust(10) + low.ljust(10) + fengli + "\t" + fengxiang)

    else:
        print("要查询的城市未找到，请检查城市名称是否正确！本程序只支持中国城市名称！")


if len(sys.argv) > 2:
    print("\n请输入正确的命令：oneweather.py [中国城市名称]，目前本程序只支持一个城市的天气询查！")
    print("如：oneweather.py 北京 , 不带城市名称，默认城市：" + city)
else:
    if len(sys.argv) == 1:

        print("\n可输入城市名参数：oneweather.py [中国城市名称/默认" + city + "],如：oneweather.py 北京")
        winfo(city)

    elif len(sys.argv) == 2:

        # 判断参数是否为汉字，只支持汉字
        for cs in range(0, len(sys.argv[1])):

            if unicodedata.east_asian_width(sys.argv[1][cs]) != 'Na':
                chz = True
            else:
                chz = False

            phz = (chz and phz)

        if not phz:
            print("\n请检查城市名称是否正确，本程序只支持中国中文城市名称！")
        else:
            city = sys.argv[1]
            winfo(city)
