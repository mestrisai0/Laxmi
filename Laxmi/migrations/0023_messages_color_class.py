# Generated by Django 3.2 on 2021-06-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laxmi', '0022_alter_messages_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='color_class',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
