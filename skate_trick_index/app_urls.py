from django.urls import path
from . import views

app_name = 'skate_trick_index'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('tricks/', views.trick_list, name='trick_list'),
] 