from django.urls import path

from serve import views

urlpatterns = [
    path('list', views.list_data, name='serve_list'),
    path('add', views.add_serve, name='serve_add'),
    path('start', views.start_serve, name='serve_start'),
    path('stop', views.stop_serve, name='serve_stop'),
    path('get', views.get_serve, name='serve_get'),
    path('terminal', views.get_serve_terminal, name='serve_terminal'),
    path('status', views.get_serve_status, name='serve_status'),
    path('connect', views.connect_token, name='connect_token')
]