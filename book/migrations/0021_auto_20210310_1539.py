# Generated by Django 3.1.1 on 2021-03-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_auto_20210310_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='major_category',
            field=models.CharField(max_length=40, verbose_name='전공 카테고리'),
        ),
    ]
