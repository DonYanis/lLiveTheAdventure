# Generated by Django 4.0.3 on 2022-04-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_tripimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='depart',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='retour',
            field=models.DateTimeField(),
        ),
    ]
