# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import psycopg2
from crawler.settings import DATABASE

class CrawlerPipeline:
    insert = '''INSERT INTO flat(flat_name, flat_image) VALUES(%s, %s)'''
    table = """ CREATE TABLE IF NOT EXISTS flat (
                flat_name VARCHAR(50),
                flat_image VARCHAR(250)
            )
            """

    def __init__(self):
        self.conn = psycopg2.connect(**DATABASE)
        self.cur = self.conn.cursor()
        self.cur.execute(self.table)

    def process_item(self, item, spider):
        self.cur.execute(self.insert, (item['name'], item['image_url']))
        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.cur.close()