# Generated by Django 4.1.5 on 2023-04-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_remove_elective_program_alter_course_semester"),
    ]

    operations = [
        migrations.AddField(
            model_name="elective",
            name="program",
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
