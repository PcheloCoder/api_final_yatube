# Generated by Django 3.2.16 on 2023-02-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_follow_following'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]