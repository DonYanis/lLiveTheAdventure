# Generated by Django 4.0.3 on 2022-04-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_rename_taken_palces_trip_taken_places_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='blog_link',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='trip',
            name='depart',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='prevoir',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='trip',
            name='prixComprend',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='trip',
            name='retour',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='program',
            field=models.TextField(default='', max_length=2000),
        ),
    ]