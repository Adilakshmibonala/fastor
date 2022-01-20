from crm.exceptions.custom_exceptions import \
    IncorrectPasswordException, UserDoesNotExistException, \
    UnexpectedErrorOccurredToGetTokenDetailsException
from crm.interactors.presenter_interfaces.login_presenter_interface\
    import LoginPresenterInterface
from crm.interactors.storage_interfaces.storage_interface import StorageInterface
from crm.interactors.dtos import EnquiryDetailsDTO


class CreateEquityDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_enquiry_details_wrapper(
            self, enquiry_details: EnquiryDetailsDTO,
            presenter: LoginPresenterInterface):
        self.create_enquiry_details(enquiry_details=enquiry_details)

    def create_enquiry_details(
            self, enquiry_details: EnquiryDetailsDTO):
        self.storage.create_enquiry_details(
            enquiry_details=enquiry_details)
