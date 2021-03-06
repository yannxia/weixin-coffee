__author__ = 'yann'

# -*- coding: utf-8 -*-
import sys, requests, json
from weixin import const
from datetime import *

header = {"apikey": const.BAIDU_API_STORE_KEY}

last_updated = {'time': None, 'date': None}


def get_weather(city='上海'):
    if city != '上海':
        try:
            result = requests.get(url='http://apis.baidu.com/heweather/weather/free', params={'city': city},
                                  headers=header).json()
            return result[list(result.keys())[0]][0]['daily_forecast'][0]
        except Exception as e:
            pass

    if last_updated['date'] is None or (datetime.now() - last_updated['time']) > timedelta(hours=1):
        result = requests.get(url='http://apis.baidu.com/heweather/weather/free', params={'city': city},
                              headers=header).json()
        key = list(result.keys())[0]
        last_updated['date'] = result[key][0]['daily_forecast'][0]
        last_updated['time'] = datetime.now()

    return last_updated['date']


def get_beauty():
    return requests.get(url="http://apis.baidu.com/txapi/mvtp/meinv", params={'num': '1'}, headers=header).json()['0']
