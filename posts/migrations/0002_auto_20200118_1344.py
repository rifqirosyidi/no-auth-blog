# Generated by Django 3.0.2 on 2020-01-18 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authors_email',
            new_name='author',
        ),
    ]
