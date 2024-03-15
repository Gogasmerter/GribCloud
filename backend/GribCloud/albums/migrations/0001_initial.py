# Generated by Django 5.0.2 on 2024-03-06 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("files", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="title")),
                ("is_public", models.BooleanField(default=False, verbose_name="is public")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="my_albums",
                        related_query_name="my_album",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="author",
                    ),
                ),
                (
                    "files",
                    models.ManyToManyField(
                        related_name="albums", related_query_name="album", to="files.file", verbose_name="files"
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="albums",
                        related_query_name="album",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="members",
                    ),
                ),
            ],
            options={
                "verbose_name": "album",
                "verbose_name_plural": "albums",
            },
        ),
    ]
