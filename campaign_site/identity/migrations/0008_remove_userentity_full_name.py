# Generated by Django 3.1.2 on 2020-11-18 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0007_auto_20201118_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userentity',
            name='full_name',
        ),
    ]