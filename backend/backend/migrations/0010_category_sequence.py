# Generated by Django 4.1.5 on 2023-03-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0009_alter_userad_code_alter_userad_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="sequence",
            field=models.PositiveIntegerField(default=0, verbose_name="Sequence"),
        ),
    ]
