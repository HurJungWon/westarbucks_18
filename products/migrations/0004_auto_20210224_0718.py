# Generated by Django 3.1.7 on 2021-02-24 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210224_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergydrink',
            old_name='dink',
            new_name='drink',
        ),
    ]