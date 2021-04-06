# Generated by Django 3.1.3 on 2021-03-26 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_auto_20210325_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='banner',
        ),
        migrations.AddField(
            model_name='tenant',
            name='address',
            field=models.CharField(blank=True, help_text='Enter business address', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tenant',
            name='industry',
            field=models.CharField(blank=True, help_text='Select a niche for your company', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='modules',
            field=models.CharField(default='CRM', help_text='Select modules you want to use', max_length=1000),
        ),
        migrations.AddField(
            model_name='tenant',
            name='number_of_staffs',
            field=models.CharField(blank=True, help_text='Enter name address', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='updated_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(help_text='Enter business name', max_length=100, unique=True),
        ),
    ]