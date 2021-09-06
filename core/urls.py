from .views import  SubscribeView, YardDataView
from django.urls import path
urlpatterns = [
    path("price/", YardDataView.as_view(), name="price_list"),
    path("subscribe/", SubscribeView.as_view(), name="subscribe")
]
