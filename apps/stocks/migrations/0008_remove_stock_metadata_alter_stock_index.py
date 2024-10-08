# Generated by Django 5.1 on 2024-09-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_alter_stock_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='metadata',
        ),
        migrations.AlterField(
            model_name='stock',
            name='index',
            field=models.IntegerField(blank=True, choices=[(1, 'KSE100'), (2, 'KSE_ALLSHR'), (3, 'KSE30'), (4, 'KMI30'), (5, 'KMI_ALLSHR'), (6, 'BKTI'), (7, 'OGTI')], default=2),
        ),
    ]
