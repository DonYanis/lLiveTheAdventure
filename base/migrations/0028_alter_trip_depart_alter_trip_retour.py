# Generated by Django 4.0.3 on 2022-04-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_alter_trip_depart_alter_trip_retour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='depart',
            field=models.DateTimeField(blank='True'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='retour',
            field=models.DateTimeField(blank='True'),
        ),
    ]