from django.contrib import admin
from crm.models import *


@admin.action(description='ClaimEnquiryDetails')
def claim_enquiry_details(modeladmin, request, queryset):
    from crm.interactors.claim_enquiry_details_interactor import \
        ClaimEnquiryDetailsInteractor
    from crm.presenters.claim_enquiry_details_presenter_implementation import \
        ClaimEnquiryDetailsPresenterImplementation
    from crm.storages.storage_implementation import StorageImplementation
    storage = StorageImplementation()
    presenter = ClaimEnquiryDetailsPresenterImplementation()
    interactor = ClaimEnquiryDetailsInteractor(storage=storage)
    user_id = str(request.user.id)

    for each_value in queryset:
        interactor.claim_enquiry_details_wrapper(
            user_id=user_id, enquiry_details_id=str(each_value.id),
            presenter=presenter)


class EnquiryDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone_number',
                    'country_code', 'course_name', 'is_public_enquiry',
                    'submitted_at']
    actions = [claim_enquiry_details]


class UserEnquiryDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'enquiry_details']


admin.site.register(UserAccount)
admin.site.register(EnquiryDetails, EnquiryDetailsAdmin)
admin.site.register(UserEnquiryDetails, UserEnquiryDetailsAdmin)
