# Generated by Django 5.0.2 on 2024-03-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0002_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="preview",
            field=models.CharField(default="", max_length=1024, verbose_name="file preview"),
            preserve_default=False,
        ),
    ]