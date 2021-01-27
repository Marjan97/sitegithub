from django.contrib import admin
from .models import UserEntity
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(UserEntity)

@admin.register(UserEntity)
class CampaignEntityAdmin(admin.ModelAdmin):
    exclude = ('groups','user_permissions','last_login','is_superuser')


    # def hero_count(self, obj):
    #     return self.model.

    # def villain_count(self, obj):
    #     return obj.villain_set.count()

    list_display = ("student_code","first_name","last_name",)





