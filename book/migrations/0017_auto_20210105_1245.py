# Generated by Django 3.1.1 on 2021-01-05 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_book_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='timeline_post/%Y/%m/%d', verbose_name='이미지'),
        ),
        migrations.AlterField(
            model_name='book',
            name='kakaoUrl',
            field=models.URLField(default='', help_text='생성한 오픈 카카오톡 링크를 작성해 주세요', verbose_name='오픈채팅 주소'),
        ),
        migrations.AlterField(
            model_name='book',
            name='major_category',
            field=models.CharField(max_length=40, verbose_name='전공 카테고리'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='가격'),
        ),
        migrations.AlterField(
            model_name='book',
            name='state',
            field=models.CharField(choices=[('최상', '최상'), ('상', '상'), ('보통', '보통'), ('하', '하')], max_length=10, verbose_name='도서 상태'),
        ),
        migrations.AlterField(
            model_name='book',
            name='writer',
            field=models.CharField(max_length=50, null=True, verbose_name='저자'),
        ),
    ]
