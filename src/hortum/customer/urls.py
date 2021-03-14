from django.urls import path

from .viewsets import CustomerRegistrationAPIView, CustomerRetriveAPIView

urlpatterns = [
	path('test/<int:pk>', CustomerRetriveAPIView.as_view()),
	path('', CustomerRegistrationAPIView.as_view()),
]
