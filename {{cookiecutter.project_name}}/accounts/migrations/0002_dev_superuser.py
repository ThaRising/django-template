from django.contrib.auth import get_user_model
from django.db import migrations


def dev_superuser(apps, schema_editor):
    user = get_user_model()
    user.objects.create_superuser(username="root", password="root")


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(dev_superuser),
    ]
