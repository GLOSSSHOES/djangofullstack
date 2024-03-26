from django.contrib import admin

from .models import StakeholderMessage


class StakeholderMessageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "message",
        "related_user",
        "user_is_anonymous",
    ]


admin.site.register(StakeholderMessage, StakeholderMessageAdmin)
