# Generated by Django 4.1 on 2023-08-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0008_alter_coursenew_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
