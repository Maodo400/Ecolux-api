# Generated by Django 4.1.1 on 2022-09-25 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recherches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='auteurs',
            field=models.ManyToManyField(null=True, to='recherches.auteur'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='classes',
            field=models.ManyToManyField(null=True, to='recherches.classe'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='maison_edition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recherches.maisonedition'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='matieres',
            field=models.ManyToManyField(null=True, to='recherches.matiere'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='type_squelette',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recherches.typesquelette'),
        ),
    ]
