import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            yield {
                'name': book.css("h3 > a::text").get(),
                'price': book.css('.product_price .price_color::text').get(),
                'url': book.css('h3 > a::attr(href)'),
            }

        next_page = response.css('li.next a ::attr(href)').get()
