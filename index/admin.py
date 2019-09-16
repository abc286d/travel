from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Activity


class ActivityAdmin(SummernoteModelAdmin):
    list_display = ("title", "updated")
    list_filter = ('created',)
    search_fields = ('title',)
    date_hierarchy = "updated"
    summernote_fields = ('body',)


admin.site.register(Activity, ActivityAdmin)
