# Generated by Django 3.1.1 on 2020-10-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201026_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.CharField(default='Konkuk', max_length=20),
        ),
    ]
