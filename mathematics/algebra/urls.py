from django.contrib import admin
from django.urls import path,include
from algebra import views
urlpatterns = [
    path('home_algebra',views.home_algebra,name='home_algebra'),
    path('secant_method',views.secant_method,name='secant_method'),
    path('bisection_method',views.bisection_method,name='bisection_method'),  
    path('newton_raphson_method',views.newton_raphson_method,name='newton_raphson_method'), 
]