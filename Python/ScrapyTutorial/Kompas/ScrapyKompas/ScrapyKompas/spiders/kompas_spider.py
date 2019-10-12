import scrapy

class kompasSpider(scrapy.Spider) :
    name = 'Kompas'
    start_urls = ['https://www.kompas.com']
    # name >> A string which defines the name for this spider
    # start_urls >> A list of URLs where the spider will begin to crawl from, when no particular URLs are specified

    def parse (self, response) :
        ## Extracting item from web
        title = response.css('title').extract()
        titleText = response.css('title::text').extract()
        yield {'title' : title, 'titleText' : titleText}

        ## Extracting index of item from web
        item1 = response.css('a.article__link::text').extract_first()
        item2 = response.css('a.article__link::text')[1].extract()
        item3 = response.css('a.article__link::text')[2].extract()
        yield {'item1' : item1, 'item2' : item2, 'item3' : item3}