# Generated by Django 4.1.5 on 2023-04-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0018_question_answer_limit_question_field_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="field_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Text", "Text"),
                    ("Number", "Number"),
                    ("Dropdown", "Dropdown"),
                    ("Toggle", "Toggle"),
                ],
                default="Text",
                max_length=128,
                null=True,
                verbose_name="Field Type",
            ),
        ),
    ]
