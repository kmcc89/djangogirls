from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('mockup', views.html_mock, name='html_mock'),
    path('mockup2', views.html_mock2, name='html_mock2'),
]