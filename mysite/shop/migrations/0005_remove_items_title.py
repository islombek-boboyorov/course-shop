# Generated by Django 3.2.5 on 2021-07-02 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210701_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='title',
        ),
    ]
