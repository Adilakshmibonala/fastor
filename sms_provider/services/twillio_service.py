class TwilioService:

    def send_message(self, phone_number: str, message: str):
        from django.http.response import HttpResponse
        return HttpResponse(content="Success", status=200)
