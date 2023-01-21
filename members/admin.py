from django.contrib import admin
from .models import Member
from .models import Employee
from .models import Person
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname' ,'lastname')

admin.site.register(Member, MemberAdmin)
admin.site.register(Employee)
admin.site.register(Person)

class PersonAdmin(ImportExportModelAdmin):
    list_display = ('name','marks')