# Generated by Django 3.1.3 on 2021-04-21 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210403_1324'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='contactinvoices', to='contact.contact'),
        ),
    ]