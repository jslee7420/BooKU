# Generated by Django 3.1.1 on 2020-12-28 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0009_auto_20201228_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='deal',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
