# Generated by Django 3.1.5 on 2021-02-05 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='year_of_exp',
            new_name='yr_of_exp',
        ),
    ]
