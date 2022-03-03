# Generated by Django 3.2.9 on 2022-03-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_category'),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
    ]
