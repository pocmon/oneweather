#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  oneweather.py
#  
#  Copyright 2015 pocmon <pocmon@sina.com> MIT License
#

import json
import urllib.request
import urllib.parse
import gzip
import sys

# 默认城市
city = '深圳'

if len(sys.argv) > 2:
    print("请输入正确的命令：oneweather.py [城市名称]")
    print("如：oneweather.py 北京 , 不带城市名称，默认城市："+city)
else:
    if len(sys.argv) == 1:
        print("可输入城市名参数：oneweather.py [城市名称]，如：oneweather.py 北京\n")
        print("默认城市："+city+"\n")
    elif len(sys.argv) == 2:
        city = sys.argv[1]
        print("\n城市："+city+"\n")

    # 网址中汉字处理，城市名称
    city = urllib.parse.quote(city)

    # 获取JSON
    url = "http://wthrcdn.etouch.cn/weather_mini?city=%s" %(city)
    mys = urllib.request.urlopen(url).read()
    # 解压JSON，并转码
    myw = gzip.decompress(mys).decode('utf-8')

    myj = json.loads(myw)

    try:
        city = myj["data"]["city"]
        wendu = myj["data"]["wendu"]
        weather = myj["data"]["ganmao"]

        print("实时天气：")
        print("\t"+(wendu+"℃ ").ljust(5)+weather+"\n")

        print("今日天气：")
        high = myj["data"]["forecast"][0]["high"]               # 最高温度
        fengxiang = myj["data"]["forecast"][0]["fengxiang"]     # 风向
        fengli = myj["data"]["forecast"][0]["fengli"]           # 风力
        type = myj["data"]["forecast"][0]["type"]               # 天气类型
        low = myj["data"]["forecast"][0]["low"]                 # 最低温度
        date = myj["data"]["forecast"][0]["date"]               # 日期
        print("\t"+date.ljust(10)+type.ljust(10)+high.ljust(10)+low.ljust(10)+fengli.ljust(8)+fengxiang)

        print("\n未来四天预报：")
        for wday in range(1,5):
            high = myj["data"]["forecast"][wday]["high"]               # 最高温度
            fengxiang = myj["data"]["forecast"][wday]["fengxiang"]     # 风向
            fengli = myj["data"]["forecast"][wday]["fengli"]           # 风力
            type = myj["data"]["forecast"][wday]["type"]               # 天气类型
            low = myj["data"]["forecast"][wday]["low"]                 # 最低温度
            date = myj["data"]["forecast"][wday]["date"]               # 日期
            print("\t"+date.ljust(10)+type.ljust(10)+high.ljust(10)+low.ljust(10)+fengli.ljust(8)+fengxiang)

        print("\n昨日天气：")
        high = myj["data"]["yesterday"]["high"]               # 最高温度
        fengxiang = myj["data"]["yesterday"]["fx"]            # 风向
        fengli = myj["data"]["yesterday"]["fl"]               # 风力
        type = myj["data"]["yesterday"]["type"]               # 天气类型
        low = myj["data"]["yesterday"]["low"]                 # 最低温度
        date = myj["data"]["yesterday"]["date"]               # 日期
        print("\t"+date.ljust(10)+type.ljust(10)+high.ljust(10)+low.ljust(10)+fengli.ljust(8)+fengxiang)

    except KeyError:
        print("要查询的城市未找到，请检查城市名称是否正确")
