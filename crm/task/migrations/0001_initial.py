# Generated by Django 3.1.3 on 2021-04-05 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tenant', '0008_auto_20210326_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('detail', models.TextField(blank=True, max_length=3000, null=True)),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('in progress', 'in progress'), ('completed', 'completed')], default='pending', max_length=500, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('custom_status', models.JSONField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedtasks', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdtasks', to=settings.AUTH_USER_MODEL)),
                ('tenant', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='tenant.tenant')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updatedtasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
