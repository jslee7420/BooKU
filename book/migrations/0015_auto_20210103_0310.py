# Generated by Django 3.1.1 on 2021-01-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_auto_20210103_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='state',
            field=models.CharField(choices=[('최상', '최상'), ('상', '상'), ('보통', '보통'), ('하', '하')], max_length=10),
        ),
    ]