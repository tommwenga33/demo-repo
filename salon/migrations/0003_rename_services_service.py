# Generated by Django 3.2.2 on 2021-05-17 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_delete_service'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
