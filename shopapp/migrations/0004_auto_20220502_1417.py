# Generated by Django 3.1 on 2022-05-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_auto_20220502_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
