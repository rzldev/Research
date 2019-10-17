import scrapy
from ..items import AmazonItem

class AmazonSpider(scrapy.Spider) :
    name = 'amazon'
    page_number = 1
    start_urls = ['https://www.amazon.com/gp/new-releases/books/?ie=UTF8&ref_=sv_b_2']

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('li.zg-item-immersion span.a-list-item div.p13n-sc-truncate.p13n-sc-line-clamp-1').css('::text').extract()
        for index, name in enumerate(product_name) :
            product_name[index] = product_name[index].strip()
        product_author = response.css('a.a-size-small.a-link-child').css('::text').extract()
        product_price = response.css('span.p13n-sc-price::text').extract()
        product_image_link = response.css('div.a-section.a-spacing-small img::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image_link'] = product_image_link

        yield items

        self.page_number += 1
        next_page = 'https://www.amazon.com/gp/new-releases/books/ref=zg_bsnr_pg_2?ie=UTF8&pg=' + str(self.page_number)

        if next_page is not None :
            yield response.follow(next_page, callback=self.parse)