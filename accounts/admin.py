from django.contrib import admin
#import from folder accounst the file models.py
from accounts.models import UserProfile

# Register your models here.
admin.site.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'phone', 'organization')
    #USER INFO instead of DESCRIPTION:
    def user_info(self, obj):
        return obj.description
    #change the title of user_info
    user_info.short_description = 'Info'

    def get_queryset(self, request):
        #inherit from method further up the chain
        #request is taken for utilizing method
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by ('-phone')
        return queryset
#use new model for User Profile
admin.site.unregister(UserProfile)
admin.site.register(UserProfile, UserProfileAdmin)