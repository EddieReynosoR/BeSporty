# Generated by Django 4.1.1 on 2022-11-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_items_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="image",
            field=models.ImageField(blank=True, upload_to="static/images/"),
        ),
        migrations.AlterField(
            model_name="items",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
