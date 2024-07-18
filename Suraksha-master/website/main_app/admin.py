from django.contrib import admin
from .models import contact

# Register your models here.
admin.site.register(contact)

from django.contrib import admin
from .models import BlockedAccount

class BlockedAccountAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'reason', 'reporter_name')  # Include 'reporter_name' in list_display
    search_fields = ('account_id', 'reason', 'reporter_name')  # Include 'reporter_name' in search_fields

admin.site.register(BlockedAccount, BlockedAccountAdmin)
