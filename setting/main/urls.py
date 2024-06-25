from django.urls import path
from . import views


urlpatterns = [
    path('', views.one, name='1'),
    path('a', views.two, name='2'),
    path('b', views.tree, name='3'),
    path('c', views.create, name='cr'),
]
