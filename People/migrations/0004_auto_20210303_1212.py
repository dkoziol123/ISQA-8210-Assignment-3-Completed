# Generated by Django 2.2 on 2021-03-03 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0003_auto_20210303_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='cell_phone',
            new_name='phone',
        ),
    ]
