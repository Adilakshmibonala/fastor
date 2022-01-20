from crm.exceptions.custom_exceptions import \
    GivenEnquiryDetailsAlreadyExistsException
from crm.interactors.presenter_interfaces.create_enquiry_details_presenter_interface \
    import CreateEquityDetailsPresenterInterface
from crm.interactors.storage_interfaces.storage_interface import StorageInterface
from crm.interactors.dtos import EnquiryDetailsDTO


class CreateEquityDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_enquiry_details_wrapper(
            self, enquiry_details: EnquiryDetailsDTO,
            presenter: CreateEquityDetailsPresenterInterface):
        try:
            self.create_enquiry_details(enquiry_details=enquiry_details)
        except GivenEnquiryDetailsAlreadyExistsException:
            return presenter.raise_given_enquiry_details_already_exists_exception()

    def create_enquiry_details(
            self, enquiry_details: EnquiryDetailsDTO):
        is_enquiry_details_already_exists = self.storage.\
            check_is_enquiry_details_already_exists(
                enquiry_details=enquiry_details)
        if is_enquiry_details_already_exists:
            raise GivenEnquiryDetailsAlreadyExistsException()

        self.storage.create_enquiry_details(enquiry_details=enquiry_details)
