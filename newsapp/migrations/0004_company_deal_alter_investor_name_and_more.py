# Generated by Django 4.1.3 on 2022-12-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsapp", "0003_investor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "last_funding_quarter",
                    models.CharField(
                        choices=[
                            ("Q1", "Q1"),
                            ("Q2", "Q2"),
                            ("Q3", "Q3"),
                            ("Q4", "Q4"),
                        ],
                        max_length=2,
                    ),
                ),
                ("last_funding_amount", models.IntegerField()),
                (
                    "last_funding_round",
                    models.CharField(
                        choices=[
                            ("PS", "Pre-Seed"),
                            ("S", "Seed"),
                            ("A", "Series A"),
                            ("B", "Series B"),
                            ("C", "Series C"),
                            ("D", "Series D"),
                            ("E", "Series E"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Subject", models.CharField(max_length=200)),
                ("Deal_Type", models.CharField(max_length=200)),
                ("Object", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="investor",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="investor",
            name="twitter_handle",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]