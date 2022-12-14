# Generated by Django 4.1.1 on 2022-11-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsClip",
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
                ("headline", models.CharField(max_length=64)),
                ("author", models.CharField(max_length=256)),
                ("publisher", models.CharField(max_length=256)),
                (
                    "industry",
                    models.CharField(
                        choices=[
                            ("ACQ", "Acquistition"),
                            ("NFUN", "New Fund"),
                            ("NFUND", "New Funding"),
                            ("O", "Other"),
                            ("BNKR", "Bankruptcy"),
                            ("MRGR", "Merger"),
                            ("SERA", "Series A"),
                            ("SERB", "Series B"),
                            ("SERC", "Series C"),
                            ("SERD", "Series D"),
                            ("SERE", "Series E"),
                        ],
                        max_length=10,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
