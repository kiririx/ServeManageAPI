from django.urls import path

from serve import views

urlpatterns = [
    path('list', views.list_data, name='serve_list'),
    path('add', views.add_serve, name='serve_add'),
    path('connect', views.connect_token, name='connect_token')
]