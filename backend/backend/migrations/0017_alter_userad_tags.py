# Generated by Django 4.1.5 on 2023-04-21 18:10

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0016_service_sequence"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userad",
            name="tags",
            field=django_mysql.models.ListCharField(
                models.CharField(max_length=10),
                blank=True,
                max_length=256,
                null=True,
                size=None,
            ),
        ),
    ]
