# -*- coding: utf-8 -*-
import scrapy
from articles.items import ArticlesItem

class BookstackSpider(scrapy.Spider):
    name = 'bookstack'
    allowed_domains = ['www.bookstack.cn']
    start_urls = ['http://www.bookstack.cn/explore?tab=recommend']

    def parse(self, response):
        
        items = []
        sites = response.css('.manual-list')
        for dl in sites.css('dl.manual-item-standard'):
            book = dl.css('.recommend-book')
            item = ArticlesItem()
            item['name'] = dl.css('.name::text').extract_first().strip()
            item['label'] = book.css('::attr(href)').extract_first().split('/')[-1]
            item['cover_url'] = book.css('img::attr(src)').extract_first().strip()
            item['author'] = 'bookstack'
            item['description'] = ''
            item['tags'] = []
            items.append(item)

        return items
