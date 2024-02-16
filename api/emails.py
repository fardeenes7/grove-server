from django.core.mail import send_mail
from django.conf import settings


def EventBookingMail(data):
    message = f'''Hello, {data['firstName']} {data['lastName']} has submitted an event booking request. 
    Here are the details:
    Name: {data['firstName']} {data['lastName']}
    Email: {data['email']}
    Phone: {data['phone']}
    Event: {data['eventType']}
    Guests: {data['guestCount']}
    Date: {data['eventDate']}
    Time: {data['eventStartTime']}
    Company: {data['companyName'] if 'companyName' in data else 'N/A'}
    '''
    send_mail(
        'Event Booking Request',
        message,
        settings.EMAIL_HOST_USER,
        settings.OWNER_EMAILS,
        fail_silently=False
    )
    return True


def SponsorshipRequestMail(data):
    message = f'''Hello, {data['name']} has submitted a sponsorship request. 
    Here are the details:
    Name: {data['name']}
    Email: {data['email']}
    Phone: {data['phone']}
    Company: {data['company'] if 'company' in data else 'N/A'}
    Message: {data['info']}
    '''
    send_mail(
        'Sponsorship Request',
        message,
        settings.EMAIL_HOST_USER,
        OWNER_EMAILS,
        fail_silently=False
    )
    return True