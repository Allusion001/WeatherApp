# Generated by Django 4.2.17 on 2025-03-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weatherApi", "0002_favorites_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="favorites",
            name="favoritesdata",
            field=models.JSONField(null=True),
        ),
    ]
