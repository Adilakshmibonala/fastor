from crm.interactors.storage_interfaces.storage_interface import StorageInterface


class SendMailToUserInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def send_mail_to_user(self, enquiry_details_id: str):
        from crm.utils.send_mail import send_email_notification

        enquiry_details = self.storage. \
            get_enquiry_details(enquiry_details_id=enquiry_details_id)
        email = enquiry_details.email
        message = 'Dear %s, \n\n We received your enquiry details, Our team is looking into it.' \
                  'We will reach you shortly.\n\n\nCordially,\n\nCustomer RelationShip Management Team\n\n' \
                  'o161623@rguktrkv.ac.in\n' % (
                    enquiry_details.username)
        send_email_notification(
            to_email=email, subject="Enquiry Details Claimed", message=message)
