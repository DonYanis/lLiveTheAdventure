# Generated by Django 4.0.3 on 2022-04-21 16:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_user_ban_reason_delete_banneduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='waitinglist',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trip',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='waitinglist', to=settings.AUTH_USER_MODEL),
        ),
    ]
