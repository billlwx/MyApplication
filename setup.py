#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/7/29

# -*- coding:utf-8 -*-
import os, time
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['platformName'] = 'Android'
# 当前设备的版本号
desired_caps['platformVersion'] = '7.0'
# 设备名可以通过 adb devices 命令来获取
desired_caps['deviceName'] = '9887a8353248344554'
# 需要调试的App 的包名
desired_caps['appPackage'] = 'com.qianjinjin.android'
# 该 App 的启动 Activity
desired_caps['appActivity'] = 'com.haohan.android.qdd.ui.activity.SplashActivity'
# 若端口未变，则为固定代码
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(10)
