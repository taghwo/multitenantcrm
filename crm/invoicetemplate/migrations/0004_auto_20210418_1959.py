# Generated by Django 3.1.3 on 2021-04-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicetemplate', '0003_auto_20210418_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicetemplate',
            name='cover',
            field=models.FileField(default='invoicetemplatecover/default.jpg', upload_to='invoicetemplatecover/'),
        ),
        migrations.AlterField(
            model_name='invoicetemplate',
            name='name',
            field=models.CharField(default='invoice/template/puritan.html', max_length=500),
        ),
    ]
