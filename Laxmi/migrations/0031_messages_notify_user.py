# Generated by Django 3.2 on 2021-06-24 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Laxmi', '0030_remove_messages_notify_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='notify_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.userprofileinfo'),
        ),
    ]
