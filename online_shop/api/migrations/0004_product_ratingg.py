# Generated by Django 3.2.9 on 2022-04-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ratingg',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]