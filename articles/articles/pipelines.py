# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class ArticlesPipeline(object):
    def process_item(self, item, spider):
        return item


class CoverImagePipeLine(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        image_url = item.get('cover_url')
        if image_url:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['cover'] = image_paths
        return item
    
