# Generated by Django 5.0.1 on 2024-02-09 16:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0018_supplieritem_created_at_supplieritem_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='modified_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
