from django.contrib import admin
from .models import page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_data')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(page,PageAdmin)