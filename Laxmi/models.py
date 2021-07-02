from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField

# # Create your models here.


class ClientName(models.Model):
    client_name = models.CharField(
        max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.client_name)


class ClientProduct(models.Model):
    product_name = models.CharField(max_length=255, null=True, blank=True)
    # product_code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    client_code = models.ForeignKey(
        ClientName, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.product_name)


class Location(models.Model):
    location_name = models.CharField(
        max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.location_name)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class PunchTable(models.Model):
    # client_id = models.ForeignKey(
    #     ClientName, on_delete=models.CASCADE, null=True, blank=True)
    client_product_id = models.ForeignKey(
        ClientProduct, on_delete=models.CASCADE, null=True, blank=True)
    punch_no = models.CharField(
        max_length=255, null=True, blank=True)  # whats this
    size = models.CharField(max_length=255, null=True, blank=True)
    ups = models.CharField(max_length=255, null=True, blank=True)  # this too
    design = models.CharField(max_length=255, null=True, blank=True)
    tuck_in_flap = models.CharField(max_length=255, null=True, blank=True)
    collar_flap = models.CharField(max_length=255, null=True, blank=True)
    cam_pam = models.CharField(
        max_length=255, null=True, blank=True)  # this too
    plate_maker = models.CharField(max_length=255, null=True, blank=True)
    plate_maker_code = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.client_product_id)


class OrderDetail(models.Model):
    Priority_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Completed', 'Completed'),
        ('Cancel', 'Cancel'),
        ('Pending', 'Pending'),
    )

    color_choice = (
        ('success', 'success'),
        ('warning', 'warning'),
        ('danger', 'danger'),
    )
    # id=models.AutoField(primary_key=True)
    punch_color = models.CharField(max_length=255, null=True, blank=True, choices=color_choice)
    plate_color = models.CharField(max_length=255, null=True, blank=True, choices=color_choice)
    plate_status = models.CharField(
         max_length=255, null=True, blank=True)  # plate&+ve field
    punch_status = models.CharField(
         max_length=255, null=True, blank=True)
    # client_name = models.ForeignKey(
    #     ClientName, on_delete=models.CASCADE, null=True, blank=True)
    client_product_id = models.ForeignKey(
        ClientProduct, on_delete=models.CASCADE, null=True, blank=True)
    # user_id = models.ForeignKey(
    #     User, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.CharField(default=False, blank=True,
                            null=True, max_length=20)
    company_box = models.CharField(
        default=False, blank=True, null=True, max_length=20)
    keyline = models.TextField(blank=True, null=True)
    negative = models.CharField(
        default=False, blank=True, null=True, max_length=20)
    positive = models.CharField(
        default=False, blank=True, null=True, max_length=20)
    proofless_file = models.CharField(
        default=False, null=True, blank=True, max_length=20)
    EMBOSE = models.CharField(default=False, null=True, blank=True, max_length=20)
    spotuv = models.CharField(default=False, null=True, blank=True, max_length=20)
    Foiling = models.CharField(
        default=False, null=True, blank=True, max_length=20)
    Perforation = models.CharField(
        default=False, null=True, blank=True, max_length=20)
    carton_style = models.CharField(
        default=False, null=True, blank=True, max_length=20)
    paper_type = models.CharField(
        default=False, null=True, blank=True, max_length=20)
    carton_size = models.TextField(blank=True, null=True)
    product_colors = models.TextField(blank=True, null=True)
    build_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.CharField(
        max_length=255, choices=Priority_CHOICES, null=True, blank=True)
    punch_available = models.BooleanField(default=False, null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdf/',null=True, blank=True)
    board_id = models.ForeignKey(
        PunchTable, null=True, blank=True, on_delete=models.CASCADE)

    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    date_completed = models.DateField(blank=True, null=True)
    punch_alert_date = models.DateField(null=True, blank=True)
    plate_and_positive_alert_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.client_product_id)

# class Notification(models.Model):
#     noti_choice = (
#         ('Punch', 'Punch'),
#         ('Plate', 'Medium'),
#     )

#     color_choice = (
#         ('orange', 'orange'),
#         ('red', 'red'),
#     )
#     when_to_send_choice = (
#         ('everyday', 'everyday'),
#         ('everytwoday', 'everytwoday'),
#         ('everythreeday', 'everythreeday'),
#     )

#     notiType = models.CharField(max_length=255, choices=noti_choice, null=True, blank=True)
#     when_to_send = models.CharField(max_length=255, choices=when_to_send_choice, null=True, blank=True)
#     color = models.CharField(max_length=255, choices=color_choice, null=True, blank=True, default='orange')
#     order_detail = models.ForeignKey(
#         OrderDetail, on_delete=models.CASCADE, null=True, blank=True)


# class LogTable(models.Model):
#     userId = models.ForeignKey(
#         User, on_delete=models.CASCADE, null=True, blank=True)
#     order_name = models.CharField(max_length=255, null=True, blank=True)
#     date = models.DateField(auto_now_add=True, null=True, blank=True)

#     def __str__(self):
#         return str(self.userId)

#     class Meta:
#         app_label = "Laxmi"


class pending_orders(models.Model):
    # client_name = models.ForeignKey(ClientName, on_delete=models.CASCADE)
    client_product_id = models.ForeignKey(
        ClientProduct, on_delete=models.CASCADE)
    pending_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

    def __str__(self):
        return str(self.client_product_id)

class Messages(models.Model):

    Subject_CHOICES = (
        ('Punch Created', 'Punch Created'),
        ('Send Order', 'Send Order'),
        ('Punch in Progress', 'Punch in Progress'),
        ('Plate Positive in Progress', 'Plate Positive in Progress'),
        ('Notification From Admin', 'Notification From Admin'),
    )

    # subject = models.CharField(max_length=40, null=True, blank=True)
    subject = models.CharField(max_length=255, choices=Subject_CHOICES, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    color_class = models.CharField(null=True, blank=True, max_length=255)
    seen = models.BooleanField(null=True, blank=True, default=False)
    created_by = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, null=True, blank=True)
    notify_user = models.CharField(null=True, blank=True, max_length=255)


    def __str__(self):
        return str(self.subject)
