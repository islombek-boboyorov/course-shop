# Generated by Django 3.2.5 on 2021-07-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_items_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(default='', upload_to='image/'),
            preserve_default=False,
        ),
    ]
