# Generated by Django 3.1.3 on 2021-03-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tenant',
            options={'ordering': ['name'], 'verbose_name_plural': 'Tenants'},
        ),
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(help_text='Enter name of tenant', max_length=100, unique=True),
        ),
    ]