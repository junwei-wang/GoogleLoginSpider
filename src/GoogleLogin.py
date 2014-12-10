# -*- coding: utf-8 -*-

"""
 * Filename:      GoogleLogin.py
 * Author:        Junwei Wang(i.junwei.wang@gmail.com)
 * Last Modified: 2014-12-10 21:37
 * Description:
"""

import scrapy
import time
import urlparse

from time import strftime

from scrapy.contrib.spiders.init import InitSpider

from scrapy.http import Request, FormRequest

from googleplaydatacrawler.items import GooglePlayAppScore


class GoogleloginSpider(InitSpider):
    name = "GoogleLogin"
    allowed_domains = ["accounts.google.com", "play.google.com"]
    login_page = 'https://accounts.google.com/ServiceLogin?hl=en_US'
    start_urls = (
        'https://play.google.com/',
    )

    def parse(self, response):
        # do parse work for each response

    def start_requests(self):
        return self.init_request()

    def init_request(self):
        return [Request(url=self.login_page, callback=self.login)]

    def login(self, response):
        return FormRequest.from_response(response,
                formdata={'Email': 'test@gmail.com',
                          'Passwd': 'test_passwd',
                          'signIn': 'Sign in'},
                callback=self.check_login_response)

    def check_login_response(self, response):
        logout_url = 'https://accounts.google.com/Logout'
        if logout_url in response.body:
            self.log("Successfully logged into Google.com at %s! Let's start "
                    "to crawel ;)" % (time.strftime('%X %x %Z')))
            yield self.make_requests_from_url(test_url) 
        else:
            self.log("Failed to log into Google.com, bad luck :(")

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
