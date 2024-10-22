import scrapy

class CarPricesSpider(scrapy.Spider):
    name = 'car_prices'
    allowed_domains = ['examplecarwebsite.com']
    start_urls = ['https://www.examplecarwebsite.com/cars-for-sale']

    def parse(self, response):
        # Loop through car listings on the page
        for car in response.css('div.car-listing'):
            yield {
                'make': car.css('span.make::text').get(),
                'model': car.css('span.model::text').get(),
                'price': car.css('span.price::text').get(),
                'year': car.css('span.year::text').get(),
                'url': response.urljoin(car.css('a::attr(href)').get()),
            }

        # Follow pagination links
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)