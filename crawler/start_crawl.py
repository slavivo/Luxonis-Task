from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.spiders.item_spider import UrlSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(UrlSpider)
process.start()