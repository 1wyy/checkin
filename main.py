# !/usr/bin/env python
# coding=utf-8
import requests
import time
import json
import sys
import os
from note163 import *
from wps import *

# 解决https访问警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

def _wps_checkin(data):
    sid = data['wps_checkin']

    print("\n            ===模拟[我的wps小程序]签到===")
    for item in sid:
        print("\n    为{}签到---↓".format(item['name']))
        wps_clockin(item['sid'])
def _wps_invite(data):
    wps_inv = data['wps_invite']

    print("\n\n            ===邀请僵尸账号获得额外会员=== ")
    for item in wps_inv:
        print("    为{}邀请---↓".format(item['name']))
        wps_invite(sid=[], invite_userid=item['invite_userid'])

def _docer_checkin(data):
    sid = data['wps_checkin']
    print("\n            ===模拟[稻壳会员]签到===")
    for item in sid:
        print("    为{}签到---↓".format(item['name']))
        docer_checkin(item['sid'])


def _youdao_checkin(data):
    print("\n\n           ===有道云笔记签到===")
    note = data['noteyoudao']
    for index,item in enumerate(note):
        YNOTE_SESS = noteyoudao(item['YNOTE_SESS'], item['user'], item['passwd'])
        if YNOTE_SESS is not None:
            # cookie失效，更新
            data['noteyoudao'][index]['YNOTE_SESS'] = YNOTE_SESS
            f = open(sys.path[0]+'/data.json', 'w', encoding="utf8",)
            json.dump(data, f, ensure_ascii=False)



if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    print("--------------------------"+now+"----------------------------")
    root_dir = os.path.split(os.path.realpath(__file__))[0]
    f = open(root_dir+'/data.json', 'r', encoding="utf8")
    data = json.load(f)
    f.close()

    _wps_checkin(data)
    _wps_invite(data)
    _youdao_checkin(data)
