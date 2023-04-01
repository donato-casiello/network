# Generated by Django 4.1.7 on 2023-04-01 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0007_alter_follower_unique_together"),
    ]

    operations = [
        migrations.RenameField(
            model_name="follower", old_name="follower", new_name="following",
        ),
        migrations.AlterUniqueTogether(
            name="follower", unique_together={("user", "following")},
        ),
    ]
