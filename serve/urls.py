from django.urls import path

from serve import views

urlpatterns = [
    path('list', views.list_data, name='serve_list'),
    path('add', views.add_serve, name='serve_add'),
    path('start', views.start_serve, name='serve_start'),
    path('get', views.get_serve, name='serve_get'),
    path('connect', views.connect_token, name='connect_token')
]