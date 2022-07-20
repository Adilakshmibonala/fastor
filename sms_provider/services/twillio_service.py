class TwilioService:

    def send_message(self, phone_number: str, message: str):
        from twilio.rest import Client
        import environ
        import sys

        env = environ.Env()
        environ.Env.read_env()
        sys.path.append('/Users/Adilakshmi Bonala/PycharmProjects/fastor/fastor')
        client = Client(env.str('TWILIO_CLIENT_ACCOUNT_ID'), env.str('TWILIO_CLIENT_AUTH_TOKEN'))
        response = client.messages.create(
            to=phone_number, from_=env.str('TWILIO_FROM_MOBILE_NUMBER'), body=message)

        return response
