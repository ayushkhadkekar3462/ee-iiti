# Generated by Django 4.1.5 on 2023-05-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research", "0005_research_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="PGLabs",
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
                ("name", models.CharField(max_length=5000)),
                ("description", models.CharField(max_length=10000)),
                ("person", models.CharField(max_length=500)),
                ("link", models.URLField()),
                ("location", models.CharField(max_length=5000)),
                ("area", models.CharField(max_length=5000)),
                ("category", models.CharField(max_length=50)),
                ("equipments", models.JSONField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Labs",
        ),
    ]
