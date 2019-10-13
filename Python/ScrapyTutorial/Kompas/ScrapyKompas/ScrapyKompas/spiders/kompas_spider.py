import scrapy

class kompasSpider(scrapy.Spider) :
    name = 'Kompas'
    start_urls = ['https://www.kompas.com']
    # name >> A string which defines the name for this spider
    # start_urls >> A list of URLs where the spider will begin to crawl from, when no particular URLs are specified

    def parse (self, response) :
        # ## Extracting item from web with css
        # title = response.css('title').extract()
        # titleText = response.css('title::text').extract()
        # yield {'title' : title, 'titleText' : titleText}
        #
        # items = response.css('a.article__link::text').extract()
        # yield {'items' : items}
        #
        # ## Extracting index of item from web
        # item1 = response.css('.article__link::text').extract_first()
        # item2 = response.css('.article__link::text')[1].extract()
        # item3 = response.css('.article__link::text')[2].extract()
        # yield {'item1' : item1, 'item2' : item2, 'item3' : item3}
        #
        # ## Extracting the value of a html text with xpath
        # item1 = response.css('a.article__link')[0].xpath('@href').extract()
        # item2 = response.css('a.article__link')[1].xpath('@href').extract()
        # item3 = response.css('a.article__link')[2].xpath('@href').extract()
        # yield {'item1' : item1, 'item2' : item2, 'item3' : item3}
        #
        # ## Extract items inside item
        # item_group = response.css('div.article__grid')[0]
        # item_title = item_group.css('a.article__link::text').extract()
        # item_tag = item_group.css('.article__subtitle::text').extract()
        # item_link = item_group.css('a.article__link').xpath('@href').extract()
        # yield {
        #     'check item title' : item_title,
        #     'item tag' : item_tag,
        #     'item link' : item_link
        # }
        #
        # item_group = response.css('div.article__grid')
        # for item in item_group :
        #     item_title = item.css('a.article__link::text').extract()
        #     item_tag = item.css('.article__subtitle::text').extract()
        #     item_link = item.css('a.article__link').xpath('@href').extract()
        #     yield {
        #         'item title' : item_title,
        #         'item tag' : item_tag,
        #         'item link' : item_link
        #     }

        ## We can extract data and place it into temporary place int items.py
        ## Create a field to specify the metadata that will be stored in items.py
        ## Import class item from items.py
        from ..items import ScrapykompasItem

        items = ScrapykompasItem()

        item_group = response.css('div.article__grid')
        for item in item_group:
            item_title = item.css('a.article__link::text').extract()
            item_tag = item.css('.article__subtitle::text').extract()
            item_link = item.css('a.article__link').xpath('@href').extract()

            ## Store all the grabbed data into items.py
            items['title'] = item_title
            items['tag'] = item_tag
            items['link'] = item_link

            ## Execute
            yield items

        ## Preccessing into the next page
        pages = response.css('li.nav__item')
        for page in pages :
            next_page = page.css('a.nav__link').xpath('@href').get()
            if next_page is not None :
                if next_page is not None :
                    yield response.follow(next_page, callback=self.parse)
