# Generated by Django 5.0.3 on 2024-03-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo_app", "0004_article_tag_alter_article_body"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="artice_post_by",
            new_name="article_post_by",
        ),
        migrations.AlterField(
            model_name="article",
            name="tag",
            field=models.CharField(
                choices=[
                    ("technology", "Technology"),
                    ("popular", "Popular"),
                    ("design", "Design"),
                ],
                max_length=20,
            ),
        ),
    ]
