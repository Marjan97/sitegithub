# Generated by Django 2.2 on 2020-12-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0011_auto_20201205_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userentity',
            options={},
        ),
        migrations.AlterModelTable(
            name='userentity',
            table='user_entity',
        ),
    ]