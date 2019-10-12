import scrapy

class kompasSpider(scrapy.Spider) :
    name = 'Kompas'
    start_urls = ['https://www.kompas.com']
    # name >> A string which defines the name for this spider
    # start_urls >> A list of URLs where the spider will begin to crawl from, when no particular URLs are specified

    def parse (self, response) :
        ## Extracting item from web with css
        title = response.css('title').extract()
        titleText = response.css('title::text').extract()
        yield {'title' : title, 'titleText' : titleText}

        items = response.css('a.article__link::text').extract()
        yield {'items' : items}

        ## Extracting index of item from web
        item1 = response.css('.article__link::text').extract_first()
        item2 = response.css('.article__link::text')[1].extract()
        item3 = response.css('.article__link::text')[2].extract()
        yield {'item1' : item1, 'item2' : item2, 'item3' : item3}

        ## Extracting the value of a html text with xpath
        item1 = response.css('a.article__link')[0].xpath('@href').extract()
        item2 = response.css('a.article__link')[1].xpath('@href').extract()
        item3 = response.css('a.article__link')[2].xpath('@href').extract()
        yield {'item1' : item1, 'item2' : item2, 'item3' : item3}