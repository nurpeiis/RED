from django.contrib import admin
from home.models import Post
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from home.models import StageOneInterests, StageOneInterestsPost
# Register your models here.
class StageOneInterestsAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'description')
    def description(self, obj):
        return obj.description
    mptt_level_indent = 20
    description.short_description = 'Sub Set'
admin.site.register(Post)
admin.site.register(StageOneInterests, StageOneInterestsAdmin,)
admin.site.register(StageOneInterestsPost)