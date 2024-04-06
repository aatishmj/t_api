from django.urls import path
from .views import create_user, submit_dashboard_data

urlpatterns = [
    path('api/create_user/', create_user, name='create_user'),
    path('api/submit_dashboard_data/', submit_dashboard_data, name='submit_dashboard_data'),
]
