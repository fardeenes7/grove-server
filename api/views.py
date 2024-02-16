# rest api
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EventBooking, SponsorshipRequest


class EventBookingView(APIView):
    def post(self, request):
        try:
            data = request.data
            EventBooking.objects.create(
                first_name=data['firstName'],
                last_name=data['lastName'],
                email=data['email'],
                phone=data['phone'],
                event=data['eventType'],
                guests=int(data['guestCount'].strip()),
                date=data['eventDate'],
                time=data['eventStartTime'],
                company_name=data['companyName'] if 'companyName' in data else None
            )
            return Response({'message': 'Event enquiry submitted. You will be contacted soon.'}, status=201)
        except Exception as e:
            return Response({'message': f'{str(e)}'}, status=400)
        

class SponsorshipRequestView(APIView):
    def post(self, request):
        try:
            data = request.data
            print(data)
            SponsorshipRequest.objects.create(
                name=data['name'],
                company=data['company'] if 'company' in data else None,
                phone=data['phone'],
                email=data['email'],
                message=data['info']
            )
            return Response({'message': 'Sponsorship request created. You will be contacted soon.'}, status=201)
        except Exception as e:
            return Response({'message': f'{str(e)}'}, status=400)
