# Generated by Django 3.2.5 on 2021-07-01 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210701_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='count',
            new_name='number',
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='about',
            table='about',
        ),
        migrations.AlterModelTable(
            name='course',
            table='course',
        ),
        migrations.AlterModelTable(
            name='items',
            table='items',
        ),
        migrations.AlterModelTable(
            name='news',
            table='news',
        ),
        migrations.AlterModelTable(
            name='subscribe',
            table='subscribe',
        ),
        migrations.AlterModelTable(
            name='video',
            table='video',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.course')),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.video')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
