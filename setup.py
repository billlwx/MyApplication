#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/7/29

# -*- coding:utf-8 -*-
import ConfigParser
import os, time
from appium import webdriver

# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
# 读取配置文件
conf = ConfigParser.SafeConfigParser()
conf.read("phone.ini")
desired_caps = {}
desired_caps['platformName'] = conf.get("samsung", "platformName")
# 当前设备的版本号
desired_caps['platformVersion'] = conf.get("samsung", "platformVersion")
# 设备名可以通过 adb devices 命令来获取
desired_caps['deviceName'] = conf.get("samsung", "deviceName")
# 需要调试的App 的包名
desired_caps['appPackage'] = conf.get("samsung", "appPackage")
# 该 App 的启动 Activity
desired_caps['appActivity'] = conf.get("samsung", "appActivity")
# Don't reset app state before this session.
desired_caps['noReset'] = conf.get("samsung", "noReset")
# 若端口未变，则为固定代码
driver = webdriver.Remote(conf.get("samsung", "driverurl"), desired_caps)
time.sleep(3)
