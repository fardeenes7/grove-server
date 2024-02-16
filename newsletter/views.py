# rest api
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subscriber


class SubscriberView(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            if Subscriber.objects.filter(email=email).exists():
                return Response({'message': 'You are already subscribed!'}, status=400)
            else:
                subscriber = Subscriber(email=email)
                subscriber.save()
                return Response({'message': 'Subscribed successfully!'}, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)
        
    def delete(self, request):
        try:
            email = request.data['email']
            try:
                subscriber = Subscriber.objects.get(email=email)
                subscriber.delete()
                return Response({'message': 'Unsubscribed successfully!'}, status=200)
            except Subscriber.DoesNotExist:
                return Response({'message': 'You are not subscribed!'}, status=400)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

