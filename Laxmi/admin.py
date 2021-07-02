from django.contrib import admin
from .models import *
# # Register your models here.


# # admin.site.register(ClientProduct)

admin.site.register(Location)

admin.site.register(UserProfileInfo)

# # admin.site.register(Status)

# admin.site.register(OrderDetail)

admin.site.register(PunchTable)

# admin.site.register(LogTable)

# # admin.site.register(CompletedOrder)

# # admin.site.register(FilePreview)

# # admin.site.register(FileTable)

# # admin.site.register(Cancel_Order)
admin.site.register(pending_orders)
admin.site.register(Messages)

class ClientProductAdmin(admin.TabularInline):
    model = ClientProduct
    extra = 0


class ClientNameAdmin(admin.ModelAdmin):
    inlines = [ClientProductAdmin]


admin.site.register(ClientName, ClientNameAdmin)


class orderDetailAdmin(admin.ModelAdmin):
    list_display = ['client_product_id','priority', 'date_completed']


admin.site.register(OrderDetail, orderDetailAdmin)
