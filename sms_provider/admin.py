from django.contrib import admin
from sms_provider.models import *


class SMSProviderConfigAdmin(admin.ModelAdmin):
    list_display = ['id', 'sms_provider', 'created_at', 'updated_at',
                    'throughput', 'is_active']


class SMSStatusDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'sms_provider', 'created_at', 'updated_at',
                    'phone_number', 'status', 'retrigger_count']


admin.site.register(UserAccount)
admin.site.register(SMSProviderConfig, SMSProviderConfigAdmin)
admin.site.register(SMSStatusDetails, SMSStatusDetailsAdmin)
