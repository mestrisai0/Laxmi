# Generated by Django 3.2 on 2021-06-17 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
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
            ],
        ),
        migrations.CreateModel(
            name='Cancel_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('product_code', models.CharField(max_length=255)),
                ('cancel_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
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
            name='CompletedOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(blank=True, max_length=240, null=True)),
                ('client_product_id', models.CharField(blank=True, max_length=240, null=True)),
                ('build_location', models.CharField(blank=True, max_length=240, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('file_preview', models.FileField(blank=True, null=True, upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='FilePreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfFile', models.FileField(upload_to='pdf/')),
                ('cdrFile', models.FileField(upload_to='cdr/')),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientname')),
                ('client_product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Laxmi.clientproduct')),
            ],
        ),
        migrations.CreateModel(
            name='FileTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255, null=True, unique=True)),
                ('file_location', models.CharField(max_length=255, null=True, unique=True)),
                ('date_field', models.DateField(auto_now_add=True, null=True)),
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
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_phase', models.CharField(blank=True, choices=[('Available', 'Available'), ('Send Order', 'Send Order'), ('Plate +ve made', 'Plate +ve made')], max_length=255, null=True)),
                ('punch_status', models.CharField(blank=True, choices=[('Available', 'Available'), ('Send Order', 'Send Order'), ('Punch made', 'Punch made')], max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
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
            name='pending_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientname')),
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
                ('colors', models.TextField(blank=True, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('current_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Completed', 'Completed')], max_length=255, null=True)),
                ('punch_available', models.BooleanField(blank=True, default=False, null=True)),
                ('alert_date', models.DateField(blank=True, null=True)),
                ('board_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.board')),
                ('build_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.location')),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientname')),
                ('client_product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientproduct')),
                ('pdf_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.filepreview')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.status')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('userId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientname'),
        ),
        migrations.AddField(
            model_name='board',
            name='client_product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.clientproduct'),
        ),
        migrations.AddField(
            model_name='board',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laxmi.location'),
        ),
    ]