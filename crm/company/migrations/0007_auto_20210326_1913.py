# Generated by Django 3.1.3 on 2021-03-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20210326_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(choices=[('technology', 'technology'), ('education', 'education'), ('ngo', 'ngo')], max_length=500),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]