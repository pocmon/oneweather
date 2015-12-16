#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------
#  Name:        oneweather2.py
#  Created:     15-12-16 pocmon
#  Edition:     Python3.4, pychrom
#  License:     MIT <http://opensource.org/licenses/MIT>
#  Copyright:   (c) pocmon <pocmon@sina.com>
#--------------------------------------------------------
#  **Note:
#  oneweather.py的v2版本，不带存储城市名称功能
#  **Warning: ...
#--------------------------------------------------------
#


import json
import urllib.request
import urllib.parse
import gzip
import tkinter


def main():
    # 主窗口，及相关属性的设置
    top_win = tkinter.Tk()
    # 窗口标题
    top_win.title('oneweather2')

    # 默认城市
    city = '深圳'

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
        # 实时天气
        wendu = myj["data"]["wendu"]+'℃'
        weather = myj["data"]["ganmao"]

        # 今日天气
        high = myj["data"]["forecast"][0]["high"]  # 最高温度
        fengxiang = myj["data"]["forecast"][0]["fengxiang"]  # 风向
        fengli = myj["data"]["forecast"][0]["fengli"]  # 风力
        type = myj["data"]["forecast"][0]["type"]  # 天气类型
        low = myj["data"]["forecast"][0]["low"]  # 最低温度
        date = myj["data"]["forecast"][0]["date"]  # 日期

        # 未来四天
        high_1 = myj["data"]["forecast"][1]["high"]  # 最高温度
        fengxiang_1 = myj["data"]["forecast"][1]["fengxiang"]  # 风向
        fengli_1 = myj["data"]["forecast"][1]["fengli"]  # 风力
        type_1 = myj["data"]["forecast"][1]["type"]  # 天气类型
        low_1 = myj["data"]["forecast"][1]["low"]  # 最低温度
        date_1 = myj["data"]["forecast"][1]["date"]  # 日期
        high_2 = myj["data"]["forecast"][2]["high"]  # 最高温度
        fengxiang_2 = myj["data"]["forecast"][2]["fengxiang"]  # 风向
        fengli_2 = myj["data"]["forecast"][2]["fengli"]  # 风力
        type_2 = myj["data"]["forecast"][2]["type"]  # 天气类型
        low_2 = myj["data"]["forecast"][2]["low"]  # 最低温度
        date_2 = myj["data"]["forecast"][2]["date"]  # 日期
        high_3 = myj["data"]["forecast"][3]["high"]  # 最高温度
        fengxiang_3 = myj["data"]["forecast"][3]["fengxiang"]  # 风向
        fengli_3 = myj["data"]["forecast"][3]["fengli"]  # 风力
        type_3 = myj["data"]["forecast"][3]["type"]  # 天气类型
        low_3 = myj["data"]["forecast"][3]["low"]  # 最低温度
        date_3 = myj["data"]["forecast"][3]["date"]  # 日期
        high_4 = myj["data"]["forecast"][4]["high"]  # 最高温度
        fengxiang_4 = myj["data"]["forecast"][4]["fengxiang"]  # 风向
        fengli_4 = myj["data"]["forecast"][4]["fengli"]  # 风力
        type_4 = myj["data"]["forecast"][4]["type"]  # 天气类型
        low_4 = myj["data"]["forecast"][4]["low"]  # 最低温度
        date_4 = myj["data"]["forecast"][4]["date"]  # 日期

        # 昨日天气
        high_z = myj["data"]["yesterday"]["high"]  # 最高温度
        fengxiang_z = myj["data"]["yesterday"]["fx"]  # 风向
        fengli_z = myj["data"]["yesterday"]["fl"]  # 风力
        type_z = myj["data"]["yesterday"]["type"]  # 天气类型
        low_z = myj["data"]["yesterday"]["low"]  # 最低温度
        date_z = myj["data"]["yesterday"]["date"]  # 日期

        # 在主窗口添加label组件
        label01 = tkinter.Label(top_win, text='城市：')
        label02 = tkinter.Label(top_win, text='实时天气：')
        label03 = tkinter.Label(top_win, text='未来四天：')
        label04 = tkinter.Label(top_win, text='昨日天气：')
        label05 = tkinter.Label(top_win, text='今日天气：')

        # label01 城市内容
        label11 = tkinter.Label(top_win, text=city)

        # 天气数据
        # label02 实时天气数据
        # 温度
        label21 = tkinter.Label(top_win, text=wendu)
        # 天气说明
        label22 = tkinter.Label(top_win, text=weather)
        # label05 今日天气
        label511 = tkinter.Label(top_win, text=date)
        label512 = tkinter.Label(top_win, text=type)
        label513 = tkinter.Label(top_win, text=high)
        label514 = tkinter.Label(top_win, text=low)
        label515 = tkinter.Label(top_win, text=fengli)
        label516 = tkinter.Label(top_win, text=fengxiang)
        # label03 未来四天数据
        label311 = tkinter.Label(top_win, text=date_1)
        label312 = tkinter.Label(top_win, text=type_1)
        label313 = tkinter.Label(top_win, text=high_1)
        label314 = tkinter.Label(top_win, text=low_1)
        label315 = tkinter.Label(top_win, text=fengli_1)
        label316 = tkinter.Label(top_win, text=fengxiang_1)
        label321 = tkinter.Label(top_win, text=date_2)
        label322 = tkinter.Label(top_win, text=type_2)
        label323 = tkinter.Label(top_win, text=high_2)
        label324 = tkinter.Label(top_win, text=low_2)
        label325 = tkinter.Label(top_win, text=fengli_2)
        label326 = tkinter.Label(top_win, text=fengxiang_2)
        label331 = tkinter.Label(top_win, text=date_3)
        label332 = tkinter.Label(top_win, text=type_3)
        label333 = tkinter.Label(top_win, text=high_3)
        label334 = tkinter.Label(top_win, text=low_3)
        label335 = tkinter.Label(top_win, text=fengli_3)
        label336 = tkinter.Label(top_win, text=fengxiang_3)
        label341 = tkinter.Label(top_win, text=date_4)
        label342 = tkinter.Label(top_win, text=type_4)
        label343 = tkinter.Label(top_win, text=high_4)
        label344 = tkinter.Label(top_win, text=low_4)
        label345 = tkinter.Label(top_win, text=fengli_4)
        label346 = tkinter.Label(top_win, text=fengxiang_4)
        # label04 昨日天气数据
        label41 = tkinter.Label(top_win, text=date_z)
        label42 = tkinter.Label(top_win, text=type_z)
        label43 = tkinter.Label(top_win, text=high_z)
        label44 = tkinter.Label(top_win, text=low_z)
        label45 = tkinter.Label(top_win, text=fengli_z)
        label46 = tkinter.Label(top_win, text=fengxiang_z)

        # 组件位置
        # 城市
        label01.grid(row=1, column=1, sticky='W')
        label11.grid(row=1, column=2, sticky='W', columnspan=3)
        # 实时天气
        label02.grid(row=2, column=1, sticky='W')
        label21.grid(row=2, column=2, sticky='W')
        label22.grid(row=2, column=3, sticky='W', columnspan=6)
        # 今日天气
        label05.grid(row=3, column=1, sticky='W')
        label511.grid(row=4, column=2, sticky='W')
        label512.grid(row=4, column=3, sticky='W')
        label513.grid(row=4, column=4, sticky='W')
        label514.grid(row=4, column=5, sticky='W')
        label515.grid(row=4, column=6, sticky='W')
        label516.grid(row=4, column=7, sticky='W')
        # 未来四天
        label03.grid(row=5, column=1, sticky='W')
        label311.grid(row=6, column=2, sticky='W')
        label312.grid(row=6, column=3, sticky='W')
        label313.grid(row=6, column=4, sticky='W')
        label314.grid(row=6, column=5, sticky='W')
        label315.grid(row=6, column=6, sticky='W')
        label316.grid(row=6, column=7, sticky='W')
        label321.grid(row=7, column=2, sticky='W')
        label322.grid(row=7, column=3, sticky='W')
        label323.grid(row=7, column=4, sticky='W')
        label324.grid(row=7, column=5, sticky='W')
        label325.grid(row=7, column=6, sticky='W')
        label326.grid(row=7, column=7, sticky='W')
        label331.grid(row=8, column=2, sticky='W')
        label332.grid(row=8, column=3, sticky='W')
        label333.grid(row=8, column=4, sticky='W')
        label334.grid(row=8, column=5, sticky='W')
        label335.grid(row=8, column=6, sticky='W')
        label336.grid(row=8, column=7, sticky='W')
        label341.grid(row=9, column=2, sticky='W')
        label342.grid(row=9, column=3, sticky='W')
        label343.grid(row=9, column=4, sticky='W')
        label344.grid(row=9, column=5, sticky='W')
        label345.grid(row=9, column=6, sticky='W')
        label346.grid(row=9, column=7, sticky='W')
        # 昨日天气
        label04.grid(row=10, column=1, sticky='W')
        label41.grid(row=11, column=2, sticky='W')
        label42.grid(row=11, column=3, sticky='W')
        label43.grid(row=11, column=4, sticky='W')
        label44.grid(row=11, column=5, sticky='W')
        label45.grid(row=11, column=6, sticky='W')
        label46.grid(row=11, column=7, sticky='W')

    else:
        tkinter.Label(top_win, text='城市无效').pack()

    # 进入无限循环
    top_win.mainloop()


# start...
if __name__ == '__main__':
    main()
