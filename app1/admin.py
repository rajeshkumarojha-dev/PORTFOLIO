from django.contrib import admin
from app1.models import Portfolio
# Register your models here.

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','description']
    