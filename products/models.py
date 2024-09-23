from django.db import models

# Create your models here.

class Product(models.Model):
    asin = models.CharField(max_length=120, unique=True, db_index=True) 
    title = models.CharField(max_length=220, blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True, default=0.00) 
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(blank=True, null=True)


class ProductScrapeEventManager(models.Manager):
    def create_scrape_event(self, data, url=None):
        asin = data.get('asin')
        if asin is None:
            return None
        product, created = Product.objects.update_or_create(
            asin=asin,
            defaults={
                "title": data.get('title') or "",
                "current_price": data.get("price") or 0.00,
                "metadata": data,
            }
        )
        event = self.create(
            product=product,
            url=url,
            data=data,
        )
        return event

class ProductScrapeEvent(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scrape_events')
    url = models.URLField(blank=True, null=True)
    asin = models.CharField(max_length=120, unique=True, db_index=True) 
    data = models.JSONField(blank=True, null=True)
    objects = ProductScrapeEventManager()