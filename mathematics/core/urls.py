from django.urls import path
from core import views,pi_search

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('register', views.register, name='register'),
    path('coomimgsoon', views.commingsoon, name='commingsoon'),
    path('finance', views.finance, name='finance'),
    path('report', views.report, name='report'),
    path('feedback', views.feedback, name='feedback'),
    path('credits', views.credits, name='credits'),
    path('about', views.about, name='about'),
    path('pi_search_method', pi_search.pi_search_method, name='pi_search_method'),
]
