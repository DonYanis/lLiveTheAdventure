# Generated by Django 4.0.3 on 2022-04-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_banneduser_delete_blacklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ban_reason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='BannedUser',
        ),
    ]
