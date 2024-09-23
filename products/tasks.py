from celery import shared_task
import helpers
from django.apps import apps

@shared_task
def scrape_product_url_task(url):
    if url is None or url == "":
        return
    ProductScrapeEvent = apps.getModel('products', 'ProductScrapeEvent')
    # open url
    html = helpers.scrape(url=url)
    #scrape url
    data=helpers.extract_amazon_product_data(html)
    #saved scraped data
    ProductScrapeEvent.objects.create_scrape_event(data, url=url)
    return

@shared_task
def scrape_products_task():
    Product = apps.getModel('products', 'Product')
    qs = Product.objects.filter(active=True)
    for obj in qs:
        url = obj.url
        scrape_product_url_task.delay(url)