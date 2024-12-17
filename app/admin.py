from django.contrib import admin
from app.models import *

# Register your models here.
class emmployee_data(admin.ModelAdmin):
    list_display=["eno",'ename','esal','eaddress']


admin.site.register(Employee,emmployee_data)
