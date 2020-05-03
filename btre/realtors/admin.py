from django.contrib import admin

from .models import Realtror

class RealtrorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'email', 'hire_date')
    list_editable = ('is_mvp',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'hire_date')
    list_per_page = 25

admin.site.register(Realtror, RealtrorAdmin)