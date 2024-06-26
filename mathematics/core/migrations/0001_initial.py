# Generated by Django 4.2.3 on 2023-12-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Credit",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=400)),
                ("links", models.CharField(max_length=200)),
                ("updated_on", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-updated_on"],
            },
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("updated_on", models.DateTimeField(auto_now_add=True)),
                ("feedback_1", models.CharField(max_length=100)),
                ("feedback_2", models.CharField(max_length=100)),
                ("first_impression", models.CharField(max_length=500)),
                ("improve_experience", models.CharField(max_length=500)),
                ("message", models.TextField()),
                ("links", models.URLField()),
            ],
            options={
                "ordering": ["-updated_on"],
            },
        ),
        migrations.CreateModel(
            name="PiSearch",
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
                ("number", models.BigIntegerField()),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="Report",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("links", models.URLField(max_length=500)),
                ("message", models.TextField()),
                ("reportfile", models.FileField(upload_to="userdata/report")),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
