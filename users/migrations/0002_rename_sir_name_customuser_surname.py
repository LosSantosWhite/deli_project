# Generated by Django 4.1 on 2022-09-01 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='sir_name',
            new_name='surname',
        ),
    ]
