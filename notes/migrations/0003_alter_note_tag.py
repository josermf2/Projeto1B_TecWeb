# Generated by Django 3.2.7 on 2021-09-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20210921_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tag',
            field=models.CharField(default='', max_length=200),
        ),
    ]
