# Generated by Django 3.0.4 on 2020-06-01 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_auto_20200528_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='passsport',
            new_name='passport',
        ),
    ]
