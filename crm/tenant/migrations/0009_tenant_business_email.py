# Generated by Django 3.1.3 on 2021-04-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0008_auto_20210326_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='business_email',
            field=models.EmailField(default='example@email.com', max_length=255),
        ),
    ]
