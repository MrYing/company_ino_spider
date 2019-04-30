# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute('scrapy crawl bafang_spider -a keyword=大数据'.split())
