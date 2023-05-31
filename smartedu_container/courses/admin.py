from django.contrib import admin

# Register your models here.

from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'avaliable')
    list_filter = ('avaliable','date' )
    # list_editable = ('name','description')
    list_display_links = ('name','description')
    search_fields = ('name','description')