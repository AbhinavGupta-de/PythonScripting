import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscraps.com"]
    start_urls = ["https://books.toscraps.com"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            yield {
                'name': book.css("h3 > a::text").get(),
                'price': book.css('.prodcut_price > p::text').get(),
                'url': book.css('h3 > a::attr(href)'),
            }
