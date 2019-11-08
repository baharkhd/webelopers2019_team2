from django.contrib import admin

# Register your models here.
from edusys.models import Course


@admin.register(Course)
class Courseadmin(admin.ModelAdmin):
    pass
