# Generated by Django 3.2.7 on 2021-09-26 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_rename_deleted_note_deleted_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deleted_Notes',
            new_name='Deleted_Note',
        ),
    ]
