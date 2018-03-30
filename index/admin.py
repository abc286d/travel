from django.contrib import admin
from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "updated")
    list_filter = ('created',)
    search_fields = ('title',)
    date_hierarchy = "updated"


admin.site.register(Activity, ActivityAdmin)
