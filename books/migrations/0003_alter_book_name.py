# Generated by Django 4.1 on 2022-09-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название книги'),
        ),
    ]