# Generated by Django 2.2 on 2021-03-04 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0004_auto_20210303_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='date',
        ),
    ]
