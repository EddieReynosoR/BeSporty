# Generated by Django 4.1.3 on 2022-11-29 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_rename_role_type_rename_role_customuser_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="address",
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]
