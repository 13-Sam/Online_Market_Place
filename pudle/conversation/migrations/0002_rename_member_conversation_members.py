# Generated by Django 4.1.7 on 2023-03-10 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='member',
            new_name='members',
        ),
    ]