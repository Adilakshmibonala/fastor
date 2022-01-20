from django.contrib import admin
from crm.models import *


class EnquiryDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone_number',
                    'country_code', 'course_name', 'is_public_enquiry',
                    'submitted_at']


class UserEnquiryDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'enquiry_details']


admin.site.register(UserAccount)
admin.site.register(EnquiryDetails, EnquiryDetailsAdmin)
admin.site.register(UserEnquiryDetails, UserEnquiryDetailsAdmin)
