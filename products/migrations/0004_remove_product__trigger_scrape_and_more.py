# Generated by Django 5.1 on 2024-09-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_active_product__trigger_scrape_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='_trigger_scrape',
        ),
        migrations.RemoveField(
            model_name='product',
            name='trigger_scrape',
        ),
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, help_text='Scrape daily?'),
        ),
    ]
