# Generated by Django 3.1.3 on 2021-03-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0005_auto_20210326_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='number_of_staffs',
            field=models.IntegerField(blank=True, default=0, help_text='Enter name address', max_length=1000, null=True),
        ),
    ]
