# Generated by Django 5.1 on 2024-09-04 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_management', '0003_alter_riskprofile_criteria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='riskprofile',
            options={'ordering': ['created_at'], 'verbose_name': 'Risk Profile', 'verbose_name_plural': 'Risk Profiles'},
        ),
    ]
