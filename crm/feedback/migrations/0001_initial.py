# Generated by Django 3.1 on 2021-10-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TimeField(max_length=3000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
