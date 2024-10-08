# Generated by Django 5.0.7 on 2024-08-27 17:58

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolios", "0002_alter_investment_options_remove_investment_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="dividends",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="brokerage_percentage",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=Decimal(
                    "0.1499999999999999944488848768742172978818416595458984375"
                ),
                max_digits=4,
                null=True,
            ),
        ),
    ]
