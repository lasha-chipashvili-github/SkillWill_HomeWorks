# Generated by Django 4.2.7 on 2023-12-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(max_length=30)),
                ('car_brand', models.CharField(max_length=60)),
                ('car_model', models.CharField(max_length=60)),
                ('car_production_year', models.IntegerField()),
            ],
        ),
    ]
