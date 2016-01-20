#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File          : tunet_login.py
# Author        : bssthu
# Project       : 
# Description   : 参考 https://net.tsinghua.edu.cn/wired/login.js
# 

import os
import urllib
import hashlib
import getpass
# try to support python2
try:
    import urllib.request as rq
    from urllib.parse import urlencode
except ImportError:
    import urllib2 as rq
    from urllib import urlencode
try:
    input = raw_input
except NameError:
    pass


# 若需记住用户信息，请修改此处
def get_user_info():
    username = get_username()
    password = get_password()
    password_md5 = get_md5(password)
    return username, password, password_md5


def main():
    # 检查是否已经在线
    if is_online():
        try_pause()
        return

    # 请求登陆
    (username, password, password_md5) = get_user_info()
    the_page = request_login(username, password_md5)

    # 结果
    print(the_page)
    if the_page == 'Login is successful.':
        pass
    elif the_page == 'IP has been online, please logout.':
        try_pause()
    else:   # fail
        try_pause()


def request_login(username, password_md5):
    url = 'https://net.tsinghua.edu.cn/do_login.php'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {
        'action': 'login',
        'username': username,
        'password': ('{MD5_HEX}%s' % password_md5),
        'ac_id': '1'
    }
    headers = {'User-Agent': user_agent}

    data = urlencode(values)
    req = rq.Request(url, data.encode('ascii'), headers)
    response = rq.urlopen(req)
    return response.read().decode()


def get_username():
    return input('user name:').strip()


def get_password():
    return getpass.getpass('password:')


def get_md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode('ascii'))
    return md5.hexdigest()


def is_online():
    if request_login('', '') == 'IP has been online, please logout.':
        print('IP has been online, please logout.')
        return True
    else:
        return False


def try_pause():
    if os.name == 'nt':
        os.system('pause')
    elif os.name == 'posix':    # linux
        pass


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print('Error: %s' % ex)
        try_pause()
