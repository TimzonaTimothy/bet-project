from django.urls import path
from .views import *

urlpatterns = [
    path('deposit/', deposit, name='deposit'),
    path('deposited/', deposit_complete, name='deposit_detail'),
]