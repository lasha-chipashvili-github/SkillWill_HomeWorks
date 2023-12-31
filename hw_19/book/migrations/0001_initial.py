# Generated by Django 4.2.7 on 2023-12-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=255)),
                ('book_author', models.CharField(max_length=255)),
                ('book_publisher', models.CharField(max_length=255)),
                ('book_number_of_pages', models.IntegerField()),
                ('book_price', models.FloatField()),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]
