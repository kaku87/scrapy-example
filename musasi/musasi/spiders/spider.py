import re
import json
from urlparse import urlparse
import urllib
import pdb
import scrapy

from scrapy.selector import Selector

try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

from musasi.items import *
from misc.log import *
from misc.spider import CommonSpider


class musasiSpider(CommonSpider):
    name = "musasi"
    allowed_domains = ["http://www.musasi.jp"]
    start_urls = [
        "http://www.musasi.jp/"
    ]
    rules = [
        Rule(sle(allow=("/explanation/[0-9]*/.*$")), callback='parse_1', follow=True),
    ]

    list_css_rules = {
        '.linkto': {
            'url': 'a::attr(href)',
            'name': 'a::text',
        }
    }

    content_css_rules = {
        'text': '#Cnt-Main-Article-QQ p *::text',
        'images': '#Cnt-Main-Article-QQ img::attr(src)',
        'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    def start_requests(self):
        return [scrapy.FormRequest("/ichikawa-chuo/login",
                                   formdata={'username': '44644', 'password': '03759'},
                                   callback=self.parse_1)]

    def parse_1(self, response):
        info('Parse ' + response.url)
        # x = self.parse_with_rules(response, self.list_css_rules, dict)
        # x = self.parse_with_rules(response, self.content_css_rules, dict)
        # print(json.dumps(x, ensure_ascii=False, indent=2))
        # pp.pprint(x)
        # return self.parse_with_rules(response, self.css_rules, musasiItem)
