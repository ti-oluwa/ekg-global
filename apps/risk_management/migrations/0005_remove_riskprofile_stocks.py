# Generated by Django 5.1 on 2024-09-14 09:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("risk_management", "0004_alter_riskprofile_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="riskprofile",
            name="stocks",
        ),
    ]
