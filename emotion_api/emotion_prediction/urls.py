from django.urls import path
from .views import predict_emotion_view

urlpatterns = [
    path('predict-emotion/', predict_emotion_view),
]
