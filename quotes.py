import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        self.log("i just visited: " + response.url)
        for quote in response.xpath("//div[@class='quote']"):
            item = {
                'author': quote.xpath(".//small[@class='author']/text()")
                .extract_first(),
                'text': quote.xpath(".//span[@class='text']/text()").
                extract_first(),
                'tags': quote.xpath('.//a[@class="tag"]/text()').extract(),
            }
            yield item
