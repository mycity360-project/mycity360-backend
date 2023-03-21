# Generated by Django 4.1.5 on 2023-02-27 21:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0003_alter_user_email_otp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email_otp",
            field=models.PositiveIntegerField(
                blank=True,
                default=0,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(111111),
                    django.core.validators.MaxValueValidator(999999),
                ],
                verbose_name="Email OTP",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_otp",
            field=models.PositiveIntegerField(
                blank=True,
                default=0,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(111111),
                    django.core.validators.MaxValueValidator(999999),
                ],
                verbose_name="Phone OTP",
            ),
        ),
    ]
