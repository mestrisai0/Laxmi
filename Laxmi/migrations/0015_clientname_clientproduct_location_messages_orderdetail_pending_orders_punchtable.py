# Generated by Django 3.2 on 2021-06-22 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Laxmi', '0014_auto_20210622_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('client_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientname')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=40, null=True)),
                ('text', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.CharField(blank=True, max_length=40, null=True)),
                ('stock_count', models.CharField(blank=True, max_length=40, null=True)),
                ('seen', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PunchTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punch_no', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('ups', models.CharField(blank=True, max_length=255, null=True)),
                ('design', models.CharField(blank=True, max_length=255, null=True)),
                ('tuck_in_flap', models.CharField(blank=True, max_length=255, null=True)),
                ('collar_flap', models.CharField(blank=True, max_length=255, null=True)),
                ('cam_pam', models.CharField(blank=True, max_length=255, null=True)),
                ('plate_maker', models.CharField(blank=True, max_length=255, null=True)),
                ('plate_maker_code', models.CharField(blank=True, max_length=255, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('client_product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientproduct')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.location')),
            ],
        ),
        migrations.CreateModel(
            name='pending_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('client_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientproduct')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('plate_status', models.CharField(blank=True, max_length=255, null=True)),
                ('punch_status', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('company_box', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('keyline', models.TextField(blank=True, null=True)),
                ('negative', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('positive', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('proofless_file', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('EMBOSE', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('spotuv', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('Foiling', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('Perforation', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('carton_style', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('paper_type', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('carton_size', models.TextField(blank=True, null=True)),
                ('product_colors', models.TextField(blank=True, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Completed', 'Completed'), ('Cancel', 'Cancel')], max_length=255, null=True)),
                ('punch_available', models.BooleanField(blank=True, default=False, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf/')),
                ('alert_date', models.DateField(blank=True, null=True)),
                ('board_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.punchtable')),
                ('build_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.location')),
                ('client_product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientproduct')),
            ],
        ),
    ]
