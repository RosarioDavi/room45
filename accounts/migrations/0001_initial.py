# Generated by Django 4.1.7 on 2023-03-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business",
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
                ("company_name", models.CharField(max_length=50)),
                ("recruiter_firstname", models.CharField(max_length=20)),
                ("recruiter_lastname", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=30)),
                ("upload_photo", models.ImageField(upload_to="")),
                ("upload_companyphoto", models.ImageField(upload_to="")),
                ("about_company", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="JobSeeker",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("about_me", models.TextField()),
                ("email", models.CharField(max_length=30)),
                ("upload_photo", models.ImageField(upload_to="")),
                ("upload_resume", models.ImageField(upload_to="")),
            ],
        ),
    ]