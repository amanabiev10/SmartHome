from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('devices/create_lamp/', views.create_lamp,  name='create_lamp'),
    path('devices/update_lamp/<int:lamp_id>/', views.update_lamp, name='update_lamp'),
]