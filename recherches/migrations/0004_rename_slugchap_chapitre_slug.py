# Generated by Django 4.1.1 on 2022-09-25 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recherches', '0003_rename_slug_chapitre_slugchap'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapitre',
            old_name='slugChap',
            new_name='slug',
        ),
    ]
