# Generated by Django 2.2 on 2020-10-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_auto_20201013_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignentity',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
        migrations.AddField(
            model_name='campaignentity',
            name='year_of_entry',
            field=models.IntegerField(null=True),
        ),
    ]