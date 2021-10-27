from core.models import PriceData,Subscribers, YardData
from core.serializers import PriceDataSerializer, SubscriberSerializer, YardDataSerializer
from typing import List
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
# Create your views here.

class YardDataView(ListAPIView):
    model = PriceData
    permission_classes = [ IsAuthenticatedOrReadOnly ]
    serializer_class = YardDataSerializer
    queryset = YardData.objects.all()
    
class SubscribeView(CreateAPIView):
    model = Subscribers
    permission_classes = [AllowAny]
    serializer_class  = SubscriberSerializer
    queryset = Subscribers.objects.all()
