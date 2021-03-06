# Generated by Django 4.0.3 on 2022-04-30 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_trip_blog_link_trip_depart_trip_prevoir_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('trip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.trip')),
            ],
        ),
    ]
