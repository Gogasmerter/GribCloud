# Generated by Django 5.0.2 on 2024-02-28 15:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file", models.CharField(max_length=1024, verbose_name="file")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        related_query_name="file",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="author",
                    ),
                ),
            ],
            options={
                "verbose_name": "file",
                "verbose_name_plural": "files",
            },
        ),
    ]
