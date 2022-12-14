# Generated by Django 4.1.1 on 2022-12-06 03:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_type_items_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name="items",
            name="quantity",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.AddField(
            model_name="items",
            name="size",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="items.size",
            ),
        ),
    ]
