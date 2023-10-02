from django.urls import path
from . import views

app_name = 'devices'

urlpatterns = [
    path('generate-api-token/', views.generate_api_token, name='generate_api_token'),
    path('my-api-token/', views.api_token_list, name='api_token_list'),
    path('devices/', views.LampList.as_view(), name='device-list'),
    path('devices/<int:pk>/', views.LampDetail.as_view(), name='device-detail'),
]