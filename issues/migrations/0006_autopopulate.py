from django.db import migrations


def populate_status(apps, schemaeditor):
    entries = {
        "To do": "An issue that is has to be solve.",
        "In progress": "An issue that is currently being solved.",
        "Done": "An issue that is already solved."
    }
    Status = apps.get_model("issues", "Status")

    for name, desc in entries.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [migrations.RunPython(populate_status)]