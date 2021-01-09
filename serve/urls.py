from django.urls import path

from serve import views

urlpatterns = [
    path('list', views.list_data, name='serve_list'),
    path('connect', views.connect_token, name='connect_token')
]