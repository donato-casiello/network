# Generated by Django 4.1.7 on 2023-04-05 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0009_remove_post_n_likes_like"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="like", unique_together={("user", "post")},
        ),
    ]
