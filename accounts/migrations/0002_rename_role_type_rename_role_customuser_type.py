# Generated by Django 4.1.3 on 2022-11-29 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Role",
            new_name="Type",
        ),
        migrations.RenameField(
            model_name="customuser",
            old_name="role",
            new_name="type",
        ),
    ]