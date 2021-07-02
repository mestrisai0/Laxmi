from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # Pages
    path('', home, name="home"),
    path('Login', Login, name="Login"),
    path('Logout', Logout, name="Logout"),
    path('new_order_page', new_order_page, name="new_order_page"),
    path('complete_order_page', complete_order_page, name="complete_order_page"),
    path('cancel_order_page', cancel_order_page, name="cancel_order_page"),
    path('pending_order_page', pending_order_page, name="pending_order_page"),
    path('notify_user_page', notify_user_page, name="notify_user_page"),

    path('punch_page', punch_page, name="punch_page"),
    path('new_punch_page', new_punch_page, name="new_punch_page"),
    path('update_punch_page/<str:pk>', update_punch_page, name="update_punch_page"),
    path('delete_punch_page/<str:pk>', delete_punch_page, name="delete_punch_page"),

    # Ajax Call
    path('get_punch_dash', get_punch_dash, name="get_punch_dash"),
    path('EditOrder', EditOrder, name="EditOrder"),
    path('loadPunch', loadPunch, name="loadPunch"),
    path('save_order_or_update_order', save_order_or_update_order, name="save_order_or_update_order"),
    path('cancel_order_ajax', cancel_order_ajax, name="cancel_order_ajax"),
    path('loadClient', loadClient, name="loadClient"),
    path('save_order_to_pending', save_order_to_pending, name="save_order_to_pending"),
    path('make_all_noti_seen', make_all_noti_seen, name="make_all_noti_seen"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
