from django.contrib import admin
from accounts.models import User, Companies
#import from folder accounst the file models.py

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'organization')
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

admin.site.register(User, UserAdmin)
admin.site.register(Companies, CompaniesAdmin)
