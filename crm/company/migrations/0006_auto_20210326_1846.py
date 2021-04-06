# Generated by Django 3.1.3 on 2021-03-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20210326_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='emails',
            field=models.JSONField(help_text='enter comma separated email address'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone_numbers',
            field=models.JSONField(blank=True, help_text='enter comma separated phone numbers address', null=True),
        ),
    ]
