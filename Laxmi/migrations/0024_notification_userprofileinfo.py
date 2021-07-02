# Generated by Django 3.2 on 2021-06-24 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Laxmi', '0023_messages_color_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Laxmi.location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notiType', models.CharField(blank=True, choices=[('Punch', 'Punch'), ('Plate', 'Medium')], max_length=255, null=True)),
                ('when_to_send', models.CharField(blank=True, choices=[('everyday', 'everyday'), ('everytwoday', 'everytwoday'), ('everythreeday', 'everythreeday')], max_length=255, null=True)),
                ('color', models.CharField(blank=True, choices=[('orange', 'orange'), ('red', 'red')], default='orange', max_length=255, null=True)),
                ('order_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.orderdetail')),
            ],
        ),
    ]