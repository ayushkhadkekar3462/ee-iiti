# Generated by Django 4.1 on 2023-08-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("achievements", "0005_alter_books_author_alter_books_publication_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patent",
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
                ("year", models.IntegerField()),
                ("name", models.CharField(max_length=5000)),
                ("pi", models.CharField(max_length=5000, null=True)),
                ("uuid", models.CharField(max_length=5000, null=True)),
                ("status", models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]
