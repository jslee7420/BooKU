# Generated by Django 3.1.1 on 2020-12-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='deal',
            field=models.CharField(default='거래중', max_length=10),
        ),
    ]
