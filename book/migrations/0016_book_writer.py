# Generated by Django 3.1.1 on 2021-01-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_auto_20210103_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
