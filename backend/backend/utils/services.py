import random

from ..constants import FROM_EMAIL
# from ..utils.google_api import send_mail


def generate_otp():
    return random.randint(111111, 999999)


def send_email(subject, body, from_email=FROM_EMAIL, to_email=()):
    print(subject)
    print(body)
    print(to_email)
    try:
        pass
        # response = send_mail(
        #     subject,
        #     body,
        #     # from_email,
        #     to_email,
        #     # fail_silently=False,
        # )
        # print(response)
    except:
        import traceback

        print(traceback.format_exc())


def send_sms():
    return
