# Generated by Django 4.2.7 on 2023-11-21 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='Title',
            new_name='title',
        ),
    ]
