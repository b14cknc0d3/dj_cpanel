from django.urls import path
from .views import CommentlistCreateView, NewsApiView,LikeCreateView

urlpatterns = [
    path("news/", NewsApiView.as_view(), name="news"),
    path("like/<int:pk>/", LikeCreateView.as_view(), name="like"),
    path("comment/<int:pk>/",CommentlistCreateView.as_view(),name="comment")
]


