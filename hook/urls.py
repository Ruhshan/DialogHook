

from django.urls import path
from .views import AirtimeRequestView
urlpatterns = [
    path('request-airtime/', AirtimeRequestView.as_view()),
]
