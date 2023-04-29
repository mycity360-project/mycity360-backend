# Generated by Django 4.1.5 on 2023-04-10 17:33

import backend.utils.services
from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0014_alter_category_icon_alter_image_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banner",
            name="image",
            field=models.ImageField(
                blank=True,
                max_length=1024,
                null=True,
                storage=gdstorage.storage.GoogleDriveStorage(),
                upload_to=backend.utils.services.get_file_path,
                verbose_name="Image",
            ),
        ),
    ]