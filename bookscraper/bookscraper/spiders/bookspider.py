import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscraps.com"]
    start_urls = ["https://books.toscraps.com"]

    def parse(self, response):
        pass
