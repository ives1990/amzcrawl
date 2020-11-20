import scrapy
import time
import re
from amzkeywords.items import AmzKeywordsItem

class KeywordsUsSpider(scrapy.Spider):
    name = 'keywords_us'
    allowed_domains = ['amazon.com']
    # start_urls = ['https://amazon.com/s?k=bottles&ref=nb_sb_noss_2']

    def start_requests(self):
        """
        docstring
        """
        urls = ['https://amazon.com/s?k=bottles&ref=nb_sb_noss_2&i=123xxx']
        for url in urls:
            print(url)
            yield scrapy.Request(url, callback=self.parse, meta= {
                # 'proxy': 'https://210.16.120.244:3128',
                'page': 1
            })

    def parse(self, response):
        
        result_box = response.css('.s-main-slot.s-result-list')

        items = []
        ranking = 1
        for row in result_box.css('.s-result-item'):
            if row.css('::attr(data-asin)'):
                item = AmzKeywordsItem()
                item['asin'] = row.css('::attr(data-asin)')
                item['product_title'] = row.css('img::attr(alt)').extract_first().strip()
                item['image_url'] = row.css('img::attr(src)').extract_first().strip()

                review_score = row.css('.a-icon-star-small span::text').extract_first().strip()
                item['review_score'] = review_score.split(' ')[0]

                review_count = row.css('a.a-section.a-spacing-top-micro .a-link-normal span::text').extract_first().strap()
                item['review_count'] = review_count

                price = row.css('a.a-price .a-offscreen::text').extract_first().strip().replace(',', '')
                priceMatch = re.match(r'^[^0-9]*([0-9|.]*)$', price)
                price = priceMatch.group(1) * 100
                item['price'] = price

                item['page'] = response.meta.get('page')
                item['page_rank'] = ranking
                item['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                ranking += 1

        return items

        
