# Generated by Django 4.0.3 on 2022-04-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_notification_options_notification_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
