from django.urls import path
from . import views

urlpatterns = [
    path('', views.gif_form, name='gif_form'),

]