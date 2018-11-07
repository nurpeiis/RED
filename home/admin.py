from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from home.models import StageOneInterests, StageOneInterestsPost
# Register your models here.
class StageOneInterestsAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'description')
    def description(self, obj):
        return obj.description
    mptt_level_indent = 20
class StageOneInterestsPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')
    

admin.site.register(StageOneInterests, StageOneInterestsAdmin,)
admin.site.register(StageOneInterestsPost,StageOneInterestsPostAdmin)