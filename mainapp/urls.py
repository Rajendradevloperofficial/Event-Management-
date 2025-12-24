from django.urls import path
from .views import (
    EventCreateAPIView,
    AlertListAPIView,
    AlertUpdateAPIView,
)

urlpatterns = [
    
    path('events/', EventCreateAPIView.as_view(), name='event-create'),

  
    path('alerts/', AlertListAPIView.as_view(), name='alert-list'),

   
    path('alerts/<int:pk>/', AlertUpdateAPIView.as_view(), name='alert-update'),
]
