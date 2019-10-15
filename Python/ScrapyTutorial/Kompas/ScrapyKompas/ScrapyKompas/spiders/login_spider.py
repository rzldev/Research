import scrapy
from scrapy.http import FormRequest
from ..items import ScrapykompasItem
from scrapy.utils.response import open_in_browser

class LoginSpider(scrapy.Spider) :
    name = 'login'
    start_urls = ['https://sso.kompas.com/login']

    # _token: RkKU9MdiqUczfVVlpYd91r97xVfLvralkK8zfWUx
    # email: amrizalrf @ gmail.com
    # password: amrizalrizkyfajar
    # service: a29tcGFz
    # continue: aHR0cDovL3d3dy5rb21wYXMuY29t

    def parse(self, response):
        my_token = response.css('form input::attr(value)').extract_first()
        my_service = response.css('form input#service::attr(value)').extract()
        my_continue = response.css('form input#continue::attr(value)').extract()
        print('token : ' + str(my_token))
        print('service : ' + str(my_service))
        print('continue : ' + str(my_continue))

        return FormRequest.from_response(response, formdata={
            '_token' : my_token,
            'email' : 'amrizalrf@gmail.com',
            'password' : 'amrizalrizkyfajar',
            'service' : my_service,
            'continue' : my_continue
        }, callback=self.start_scraping)

    def start_scraping(self, response) :
        open_in_browser(response)

        item_group = response.css('div.article__grid')
        for item in item_group:
            my_response = response.css('body').extract()
            print(my_response)