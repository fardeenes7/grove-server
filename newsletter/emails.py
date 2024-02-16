#emails.py
from django.core.mail import send_mail
from django.conf import settings

def SubscriberMail(data):
    message = f'''Hello, {data['email']} has subscribed to your newslettter. 
    Here are the details:
    Email: {data['email']}
    '''
    send_mail(
        'New Subscription',
        message,
        settings.EMAIL_HOST_USER,
        settings.OWNER_EMAILS,
        fail_silently=False
    )
    return True