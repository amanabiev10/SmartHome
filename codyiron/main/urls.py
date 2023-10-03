from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('devices/create_lamp/', views.create_lamp,  name='create_lamp'),
    path('toggle-lamp/<int:lamp_id>/', views.toggle_lamp, name='toggle_lamp'),
    path('update-brightness/<int:lamp_id>/', views.update_brightness, name='update_brightness'),
    path('update-color/<int:lamp_id>/', views.update_color, name='update_color'),
]