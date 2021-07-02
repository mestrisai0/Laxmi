from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .forms import PunchForm
# Count imported
from django.db.models import Count
# Imported Models
from .models import *
# from .uploadForm import UploadForm
import csv
from django.http import HttpResponse
import datetime
# Exporting PDF and CSV
from django.http import JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
# User Authentication
from django.contrib.auth.admin import User
from django.contrib.auth.admin import Group
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models import Q
from django.conf import settings
from django.core.paginator import Paginator
from .decorators import *
from django.contrib import messages

# Helper fun
from .helper_func import *
# Create your views here.


# Pages

@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        try:
            user = authenticate(request, username=u,password=p)
            print(user)
            print(user.id)
            
            if user is not None:
                login(request,user)
                # register = Register.objects.get(user = user.id)
                # status = register.status
                # if status == 'Approved':
                return redirect('home')
                # else:
                #     messages.error(request, 'You are not approved')
                    
            else:
                messages.warning(request,'Email Id or Password is Wrong')
        except:
            messages.warning(request, 'Email Id or Password is Wrong')
            # print('nothing happend')
    d = {}
    return render(request,'Laxmi/LoginPage/login.html')


def Logout(request):
    logout(request)
    return redirect('Login')

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='Login')
def home(request):
    pagename = 'Dashboard'
    all_ms, ms_count = common_notification_model_fetch(request)

    orders = OrderDetail.objects.filter(~Q(priority='Completed') & ~Q(priority='Cancel') & ~Q(priority='Pending')) 
    all_location = Location.objects.all()
    order_send_order_warning_punch = OrderDetail.objects.filter(Q(punch_status='Send Order') & Q(punch_color='warning')).count()
    order_send_order_danger_punch = OrderDetail.objects.filter(Q(punch_status='Send Order') & Q(punch_color='danger')).count()
    order_progress_warning_punch = OrderDetail.objects.filter(Q(punch_status='Punch in Progress') & Q(punch_color='warning')).count()
    order_progress_danger_punch = OrderDetail.objects.filter(Q(punch_status='Punch in Progress') & Q(punch_color='danger')).count()
    
    lst_to_pass = [order_send_order_warning_punch, order_send_order_danger_punch, order_progress_warning_punch, order_progress_danger_punch]

    order_send_order_warning_plate = OrderDetail.objects.filter(Q(plate_status='Send Order') & Q(plate_color='warning')).count()
    order_send_order_danger_plate = OrderDetail.objects.filter(Q(plate_status='Send Order') & Q(plate_color='danger')).count()
    order_progress_warning_plate = OrderDetail.objects.filter(Q(plate_status='Plate Positive in Progress') & Q(plate_color='warning')).count()
    order_progress_danger_plate = OrderDetail.objects.filter(Q(plate_status='Plate Positive in Progress') & Q(plate_color='danger')).count()
    
    lst_to_pass_plate = [order_send_order_warning_plate, order_send_order_danger_plate, order_progress_warning_plate, order_progress_danger_plate]

    context = {
        'pagename': pagename,
        'orders': orders,
        'ms_count': ms_count,
        'messages': all_ms,
        'location':all_location,
        'lst_to_pass':lst_to_pass,
        'lst_to_pass_plate':lst_to_pass_plate,
    }

    return render(request, 'Laxmi/DashboardPage/dashboard_page.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='Login')
def complete_order_page(request):
    # complete = CompletedOrder.objects.all().order_by("-date_completed")
    co = OrderDetail.objects.filter(priority='Completed') 
    all_ms, ms_count = common_notification_model_fetch(request)

    context = {
        'complete': co,
        'ms_count': ms_count,
        'messages': all_ms,
    }

    return render(request, 'Laxmi/CompleteOrderPage/complete_order.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='Login')
def cancel_order_page(request):
    # complete = CompletedOrder.objects.all().order_by("-date_completed")
    co = OrderDetail.objects.filter(priority='Cancel') 
    all_ms, ms_count = common_notification_model_fetch(request)

    context = {
        'complete': co,
        'ms_count': ms_count,
        'messages': all_ms,
    }

    return render(request, 'Laxmi/CancelOrderPage/cancel_order.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='Login')
def pending_order_page(request):
    # complete = CompletedOrder.objects.all().order_by("-date_completed")
    co = OrderDetail.objects.filter(priority='Pending') 
    all_location = Location.objects.all()
    all_ms, ms_count = common_notification_model_fetch(request)

    context = {
        'complete': co,
        'ms_count': ms_count,
        'messages': all_ms,
        'location':all_location
    }

    return render(request, 'Laxmi/PendingOrderPage/pending_order_page.html', context)


def get_matched_element(strings, element=None, page=1):
    matched_found = []
    result = dict()
    if element is None:
        start = (page - 1) * 10
        end = 10 * page
        for each_element in strings[start:end]:
            matched_found.append(
                {'id': str(each_element), 'text': str(each_element)})
        return {"results": matched_found, "count_filtered": len(strings) - page*10, "datasent": len(matched_found)}

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='Login')
def new_order_page(request):
    # clients = ClientName.objects.all()
    all_location = Location.objects.all()
    all_ms, ms_count = common_notification_model_fetch(request)

    if request.is_ajax():
        try:
            page = int(request.GET.get('page'))
        except:
            page = 1
        element = request.GET.get('term')
        result = ClientName.objects.all()
        content = get_matched_element(result, element, page)
        return JsonResponse(content, safe=False)

    context = {
        # 'clients':clients,
        'ms_count': ms_count,
        'messages': all_ms,
        'location':all_location,
    }

    return render(request, 'Laxmi/NewOrderPage/new_order_page.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='Login')
def notify_user_page(request) : 
    users = UserProfileInfo.objects.filter(~Q(designation='Manager'))
    all_ms, ms_count = common_notification_model_fetch(request)

    if request.method == 'POST':
        name = request.POST.get('notify_user', 0)
        desc = request.POST.get('notify_description', 0)

        subject = 'Notification From Admin'
        text = desc
        color_class = 'notification_danger'
        single_user = User.objects.filter(username='admin')
        userProfile = UserProfileInfo.objects.filter(user=single_user[0].id)
        
        create_notification(subject, text, color_class, userProfile[0], name)


    context = {
        'users' : users,
        'ms_count': ms_count,
        'messages': all_ms,
    }
    return render(request, 'Laxmi/AdminRightPage/notify_user.html', context)

@login_required(login_url='Login')
def punch_page(request):
    if request.user.username == 'admin':
        punch_data = PunchTable.objects.all()
    else:
        single_user = User.objects.filter(username=request.user)
        userProfile = UserProfileInfo.objects.filter(user=single_user[0].id)
        location_instance = userProfile[0].location
        punch_data = PunchTable.objects.filter(location=location_instance)
    all_ms, ms_count = common_notification_model_fetch(request)

    context = {
        'punch_data':punch_data,
        'ms_count': ms_count,
        'messages': all_ms,
    }

    return render(request, 'Laxmi/PunchPage/punch_page.html', context)

@login_required(login_url='Login')
def new_punch_page(request):
    punch_form = PunchForm()
    all_ms, ms_count = common_notification_model_fetch(request)

    if request.method == 'POST':
        form = PunchForm(request.POST)
        if form.is_valid():
            form.save()

            new_noti = Messages.objects.create()
            lastest_punch = PunchTable.objects.last()
            user_name = request.user
            single_user = User.objects.filter(username=user_name)
            userProfile = UserProfileInfo.objects.filter(user=single_user[0].id)
            subject = 'plate Created'
            text = f'plate created of size {lastest_punch.punch_no} by user {user_name} at location {lastest_punch.location.location_name}'
            color_class = 'notification_success'
            
            create_notification(subject, text, color_class, userProfile[0], 'admin')

            # noti_to_consumer(color_class, text, subject)
            return redirect('punch_page')

    if request.user.username == 'admin':
        location_name = 'all'
    else:
        single_user = User.objects.filter(username=request.user)
        userProfile = UserProfileInfo.objects.filter(user=single_user[0].id)
        location_name = userProfile[0].location.location_name


    context = {
        'punch_form':punch_form,
        'location_name':location_name,
        'ms_count': ms_count,
        'messages': all_ms,
    }

    return render(request, 'Laxmi/PunchPage/add_new_punch.html', context)

@login_required(login_url='Login')
def update_punch_page(request, pk):
    punch_data = PunchTable.objects.get(id=pk)
    punch_form = PunchForm(instance=punch_data)
    all_ms, ms_count = common_notification_model_fetch(request)

    if request.method == 'POST':
        form = PunchForm(request.POST, instance=punch_data)
        if form.is_valid():
            form.save()
            return redirect('punch_page')           

    context = {
        'punch_form':punch_form,
        'ms_count': ms_count,
        'messages': all_ms,
    }

    return render(request, 'Laxmi/PunchPage/add_new_punch.html', context)

@login_required(login_url='Login')
def delete_punch_page(request, pk):
    punch_data = PunchTable.objects.get(id=pk)

    punch_data.delete()
    return redirect('punch_page')






# Ajax Call

def get_punch_dash(request):
    sid = request.GET['sid']
    availabe_punch_dash = list(PunchTable.objects.filter(id=sid).values())
    print(availabe_punch_dash)
    return JsonResponse({'status': 'Save', 'data_form': availabe_punch_dash})    


def EditOrder(request):
    id = request.GET['sid']
    print(id, 'vndkvndjn')
    eo = list(OrderDetail.objects.filter(id=id).values())
    bo = OrderDetail.objects.get(id=id).board_id

    product_name_instance = ClientProduct.objects.get(id=eo[0]['client_product_id_id'])
    product_name_pass = product_name_instance.product_name
    client_name_pass = product_name_instance.client_code.client_name
    try:
        location_instance = Location.objects.get(id=eo[0]['build_location_id'])
        location_pass = location_instance.location_name
    except:
        location_pass = ''
    content = {
        'status': 'Save', 
        'data_form': eo, 
        # 'bi':bi,
        'client_name_pass':client_name_pass,
        'product_name_pass':product_name_pass,
        'location_pass':location_pass,
    }
    # fname = f.pdfFile
    # print(fname)
    return JsonResponse(content)


def loadPunch(request):
    if request.method == 'GET':
        id = request.GET['id']
        availabe_punch = list(PunchTable.objects.filter(id=id).values())
        return JsonResponse({'status': 'Save', 'data_id': availabe_punch})

    if request.is_ajax() and request.method == 'POST':
        # print("i am here in boards ajax")
        punch_check = request.POST['punches'] 

        availabe_punch = list(PunchTable.objects.filter(
            punch_no=punch_check).values())
        print(availabe_punch)
        punches = "" if availabe_punch is None else availabe_punch
    content = {
        'response_punches': punches,
    }

    return JsonResponse(content, safe=False)


def save_order_to_pending(request):
    _, client_name_new, new_client_product = client_name_product_helper(request)
    client_product_name_new = ClientProduct.objects.filter(product_name=new_client_product, client_code=client_name_new)
    order = OrderDetail.objects.create()
    order.client_product_id = client_product_name_new[0]
    order.priority = 'Pending'
    order.save()

    return JsonResponse({"data": 'Saved to Pedning'})


def save_order_or_update_order(request):

    _, client_name_new, new_client_product = client_name_product_helper(request)

    client_product_name_new = ClientProduct.objects.filter(product_name=new_client_product, client_code=client_name_new)

    # client_product_name_new = ClientProduct.objects.get(product_name=new_client_product)

    location = request.POST['location']
    sid = request.POST['sid']
    priority = request.POST['job_priority']
    logo = request.POST['logo']
    company_box = request.POST['company_box']
    keyline = request.POST['keyline']
    negative = request.POST['negative']
    positive = request.POST['positive']
    proofless_file = request.POST['proofless_file']
    embose = request.POST['embose']
    spotuv = request.POST['spotuv']
    foiling = request.POST['foiling']
    perforation = request.POST['perforation']
    carton_style = request.POST['carton_style']
    paper_type = request.POST['paper_type']
    colors = request.POST['colors']
    board_id = request.POST['board_id_new']
    due_date = request.POST['due_date']
    punch_status = request.POST['punch_status']
    plate_and_positive_status = request.POST['plate_and_positive_status']

    if sid == 'create':
        order = OrderDetail.objects.create()
        order.client_product_id = client_product_name_new[0]
    else:
        order = OrderDetail.objects.get(id=sid)

    if punch_status == 'Available':   
        order.punch_alert_date =  None
        order.punch_color = 'success'
    else:
        order.punch_alert_date = (date.today()+timedelta(days=1)).isoformat()
        order.punch_color = 'warning'

    if plate_and_positive_status == 'Available':   
        order.plate_and_positive_alert_date =  None
        order.plate_color = 'success'
    else:
        order.plate_and_positive_alert_date = (date.today()+timedelta(days=1)).isoformat()
        order.plate_color = 'warning'

    if due_date:
        order.due_date = due_date


    try:
        loc = Location.objects.get(location_name=location)
        order.build_location = loc
    except:
        loc = ''

    if priority == 'Completed':
        order.date_completed = timezone.now()

    if board_id:
        board_id = PunchTable.objects.get(id=board_id)
        order.board_id = board_id     

    try:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    except:
        myfile = ""

    order.logo = logo
    order.company_box = company_box
    order.company_box = company_box
    order.proofless_file = proofless_file
    order.priority = priority
    order.keyline = keyline
    order.negative = negative
    order.positive = positive
    order.EMBOSE = embose
    order.spotuv = spotuv
    order.Foiling = foiling
    order.Perforation = perforation
    order.carton_style = carton_style
    order.paper_type = paper_type
    order.colors = colors
    order.punch_status = punch_status
    order.plate_status = plate_and_positive_status
    

    if myfile:
        order.pdf_file = myfile
        
    order.save()

    return JsonResponse({"msg": 'order save'})

def cancel_order_ajax(request):
    # complete = CompletedOrder.objects.all().order_by("-date_completed")
    print('in cancel order')
    sid = request.GET['sid']
    order = OrderDetail.objects.get(id=sid)
    order.priority = 'Cancel'
    order.save()

    context = {
        'msg': 'Order priority shifted to cancel',
    }

    return JsonResponse(context)



def loadClient(request):
    if request.is_ajax() and request.method == 'POST':
        selected_client = request.POST['client']
        client_product = ClientProduct.objects.all()
        response_products = []
        for i in client_product:
            if str(i.client_code) == selected_client:
                response_products.append(i.product_name)
        content = {
            'response_products': response_products,
        }
    return JsonResponse(content, safe=False)


def make_all_noti_seen(request):
    messages = Messages.objects.filter(seen__exact='False')
    messages = Messages.objects.filter(Q(notify_user=request.user) & Q(seen__exact='False'))
    messages.update(seen=True) 

    context = {
        'msg':'set all to true'
    }

    return JsonResponse(context)

