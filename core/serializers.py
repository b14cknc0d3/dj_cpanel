from rest_framework import serializers
from .models import PriceData,Subscribers, YardData

class PriceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceData
        fields = ("price","limit")

class YardDataSerializer(serializers.ModelSerializer):
    buy = PriceDataSerializer()
    sell = PriceDataSerializer()
    class Meta:
        model = YardData
        fields = ("yard","buy","sell","youtube_id","timestamp")
        
class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = ("email",)
