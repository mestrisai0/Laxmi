# Generated by Django 3.2 on 2021-06-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laxmi', '0007_remove_completedorder_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='current_date',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
