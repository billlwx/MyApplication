#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/7/27

import unittest
from time import sleep

import setup
import swipe


class Login(unittest.TestCase):

    def test_login(self):
        swipe.swipLeft(1000)
        sleep(3)
        swipe.swipLeft(1000)
        sleep(3)
        # 点击立即体验
        setup.driver.find_element_by_id('com.qianjinjin.android:id/clickView').click()
        sleep(3)
        swipe.swipeDown(500)
        sleep(3)
        swipe.swipRight(500)
        sleep(3)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/gotologin_tv').click()
        setup.driver.find_element_by_id('com.qianjinjin.android:id/mobileInput').send_keys('******')
        sleep(3)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/pwdInput').send_keys('t11111')
        setup.driver.find_element_by_id('com.qianjinjin.android:id/loginBtn').click()
        sleep(3)
        try:
            setup.driver.find_element_by_id('com.qianjinjin.android:id/msg_adv_close').click()
        except:
            print 'failed'
            pass
        swipe.swipRight(500)
        sleep(3)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/itemDesc').click()
        sleep(3)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/logoutBtn').click()
        sleep(3)

            #
        # setup.driver.find_element_by_id('com.qianjinjin.android:id/actionBtn').click()
        # sleep(3)

if __name__ == '__main__':
        unittest.main()