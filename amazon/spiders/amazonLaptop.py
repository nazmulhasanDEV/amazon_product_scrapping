import scrapy


class AmazonlaptopSpider(scrapy.Spider):
    name = 'amazonLaptop'
    allowed_domains = ['amazon.com/']
    start_urls = ['https://www.amazon.com/s?k=laptops&i=computers-intl-ship&ref=nb_sb_noss']

    def parse(self, response):
        for x in response.xpath("//div[@class='a-section a-spacing-none']/h2/a/span[@class='a-size-medium a-color-base a-text-normal']"):
            yield {
                'title' : x.xpath(".//text()").get()
            }
