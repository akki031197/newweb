# Generated by Django 2.2.12 on 2020-04-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.CharField(max_length=1000),
        ),
    ]
