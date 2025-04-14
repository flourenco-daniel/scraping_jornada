import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook?sb=rb#D[A:notebook]"]

    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            

            prices = product.css('span.andes-money-amount__fraction::text').getall()

            #o yield aloca os dados na memoria para retornar todos os outputs do loop for de uma vez só
            yield{
                'brand':product.css('span.poly-component__brand::text').get(),
                'description':product.css('a.poly-component__title::text').get(),
                'seller':product.css('span.poly-component__seller::text').get(),
                'rating':product.css('span.poly-reviews__rating::text').get(),
                'currency':product.css('span.andes-money-amount__currency-symbol::text').get(),
                'old_value':prices[0] if len (prices) > 0 else None,
                'new_value':prices[1] if len (prices) > 0 else None
            }

        pass
