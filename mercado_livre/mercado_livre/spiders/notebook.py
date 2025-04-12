import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook?sb=rb#D[A:notebook]"]

    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            
            yield{
                'brand':product.css('span.poly-component__brand::text').get(),
                'description':product.css('a.poly-component__title::text').get(),
                'seller':product.css('span.poly-component__seller::text').get(),
                'rating':product.css('span.poly-reviews__rating::text').get(),
                'currency':product.css('span.andes-money-amount__currency-symbol').get(),
                'value':product.css('span.andes-money-amount__fraction').get()
            }

        pass
