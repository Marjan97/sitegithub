# Generated by Django 3.1.2 on 2020-11-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0008_remove_userentity_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentity',
            name='mobile_phone_number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=12, null=True),
        ),
    ]
