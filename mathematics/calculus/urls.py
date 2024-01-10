from django.contrib import admin
from django.urls import path
from calculus import views
urlpatterns = [
    path('home_calculus',views.home_calculus,name='home_calculus'),
    path('indefinite_integral',views.indefinite_integral,name='indefinite_integral'),

]