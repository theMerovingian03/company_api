# Generated by Django 5.1.2 on 2024-11-03 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="employee",
            options={"ordering": ["id"]},
        ),
    ]