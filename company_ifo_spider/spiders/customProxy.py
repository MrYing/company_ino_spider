# -*- coding: utf-8 -*-

import requests


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = self.get_proxy().decode("utf-8")
        request.meta['proxy'] = 'http://%s' % proxy

    def get_proxy(self):
        return requests.get("http://120.221.19.38:50100/get/").content
