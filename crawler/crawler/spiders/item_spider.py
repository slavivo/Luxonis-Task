import scrapy 
import json
from crawler.items import CrawlerItem


class FlatSpider(scrapy.Spider):
    name = 'flat_spider'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']
    required_count = 500
    headers = {
        'authority': 'www.sreality.cz',
        'method': 'GET',
        'path': '/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=20&tms=1659510233485',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'per_page=20; lps=eyJfZnJlc2giOmZhbHNlLCJfcGVybWFuZW50Ijp0cnVlfQ.Yuo1fg.72Fcly_XLfxfbkukup7WG4eLLuk',
        'pragma': 'no-cache',
        'referer': 'https://www.sreality.cz/hledani/prodej/byty',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }

    def parse(self, response):
        url_first = 'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page='
        url_second = '&per_page=20&tms=1659510091688'
        for i in range(self.required_count // 20):
            yield scrapy.Request(url_first + str(i + 1) + url_second, callback=self.parse_api, headers=self.headers)

    def parse_api(self, response):
        data = json.loads(response.body)
        for flat in data['_embedded']['estates']:
            print(flat['name'])
            item = CrawlerItem()
            item['name'] = flat['name']
            item['image_url'] = flat['_links']['images'][0]['href']
            yield item
