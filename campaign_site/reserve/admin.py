from django.contrib import admin
from import_export import resources, fields
from .models import RegisteredUsersEntity, CampaignEntity
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from rest_framework.authtoken.models import Token
# Register your models here.
from import_export.fields import Field
# admin.site.register(RegisteredUsers)
admin.site.unregister(Group)
admin.site.unregister(Token)



class ExportData(resources.ModelResource):
    name=fields.Field()

    class Meta:
        model = CampaignEntity
        # fields = ('name',)


    # def export(self, queryset=None, *args, **kwargs):
    #     queryset = CampaignEntity.objects.filter(id__in[1])
    #     return ExportData().export(queryset)




@admin.register(CampaignEntity)
class CampaignEntityAdmin(ImportExportModelAdmin):
    re_mo=ExportData


    list_display = ("name","execution_date","is_registered","rest_capacity","is_canceled","year_of_entry",)
    list_filter = ("execution_time","is_canceled","year_of_entry",)


@admin.register(RegisteredUsersEntity)
class RegisteredUsersAdmin(admin.ModelAdmin):
    list_per_page = 1
    # list_filter = ("year",)
    list_display = ("student","campaign",)

