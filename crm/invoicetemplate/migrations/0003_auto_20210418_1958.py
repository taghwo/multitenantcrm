# Generated by Django 3.1.3 on 2021-04-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicetemplate', '0002_auto_20210418_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicetemplate',
            name='content',
        ),
        migrations.AlterField(
            model_name='invoicetemplate',
            name='cover',
            field=models.FileField(default='invoice/template/puritan.html', upload_to='invoicetemplatecover/'),
        ),
    ]
