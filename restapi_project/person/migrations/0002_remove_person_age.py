# Generated by Django 4.2.5 on 2023-09-12 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="person", name="age",),
    ]
