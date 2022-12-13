from django.db import migrations

def populate_types(apps, schemaeditor):
    entries = {
        "Sneakers":"Basic Sneakers.",
        "Exercise":"Excercise cloaths.",
        "Sport":"Sportswear.",
        "Jerseys":"Shirts"
    }
    Types = apps.get_model("items", "Type")
    for name, desc in entries.items():
        status_obj = Types(name=name)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [migrations.RunPython(populate_types)]