# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmzKeywordsItem(scrapy.Item):
    asin = scrapy.Field()
    product_title = scrapy.Field()
    image_url = scrapy.Field()
    review_score = scrapy.Field()
    review_count = scrapy.Field()
    price = scrapy.Field()
    page_rank = scrapy.Field()
    page = scrapy.Field()
    created_at = scrapy.Field()
