# Generated by Django 4.1.5 on 2023-08-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0007_user_blocked_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="price_limit",
            field=models.FloatField(blank=True, null=True, verbose_name="Price Limit"),
        ),
    ]
