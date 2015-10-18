#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File          : tunet_login.py
# Author        : bssthu
# Project       : 
# Description   : 参考 https://net.tsinghua.edu.cn/wired/login.js
# 

import os, sys
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
def getUserInfo():
    username = getUsername()
    password = getPassword()
    passwordMd5 = getMd5(password)
    return (username, password, passwordMd5)


def main():
    # 检查是否已经在线
    if isOnline():
        tryPause()
        return

    # 请求登陆
    (username, password, passwordMd5) = getUserInfo()
    the_page = requestLogin(username, passwordMd5)

    # 结果
    print(the_page)
    if the_page == 'Login is successful.':
        pass
    elif the_page == 'IP has been online, please logout.':
        tryPause()
    else:   # fail
        tryPause()


def requestLogin(username, passwordMd5):
    url = 'https://net.tsinghua.edu.cn/do_login.php'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {
        'action' : 'login',
        'username' : username,
        'password' : ('{MD5_HEX}%s' % passwordMd5),
        'ac_id' : '1'
    }
    headers = { 'User-Agent' : user_agent }

    data = urlencode(values)
    req = rq.Request(url, data.encode('ascii'), headers)
    response = rq.urlopen(req)
    return response.read().decode()


def getUsername():
    return input('user name:').strip()


def getPassword():
    return getpass.getpass('password:')


def getMd5(text):
    md5 = hashlib.md5()
    md5.update(text.encode('ascii'))
    return md5.hexdigest()


def isOnline():
    if requestLogin('', '') == 'IP has been online, please logout.':
        print('IP has been online, please logout.')
        return True
    else:
        return False


def tryPause():
    if os.name == 'nt':
        os.system('pause')
    elif os.name == 'posix':    # linux
        pass


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print('Error: %s' % ex)
        tryPause()
