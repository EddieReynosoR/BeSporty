from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "Default":"Basic Customer.",
        "Premium":"VIP Customer.",
        "Administrator":"Workers of the company managin the page."
    }
    # Types = apps.get_model("accounts", "Type")
    # for name, desc in entries.items():
    #     status_obj = Types(name=name)
    #     status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [migrations.RunPython(populate_status)]