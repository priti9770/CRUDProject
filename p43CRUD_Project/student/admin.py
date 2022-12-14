from django.contrib import admin

# Register your models here.
from .models import user
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ('id','name','email','password','gender','birth_date')

    # 1.--> py manage.py makemigrations
    # 2.--> py manage.py migrate
    #3.-->  py manag.py createsuperuser