from django.contrib import admin
from django.urls import path
from numerical_analysis import views
urlpatterns = [
    path('home_numerical_integration',views.home_numerical_integration,name='home_numerical_integration'),
    path('home_numerical_differentiation',views.home_numerical_differentiation,name='home_numerical_differentiation'),
    path('trapezoidal_method',views.trapezoidal_method,name='trapezoidal_method'),
    path('simpson_3_method',views.simpson_3_method,name='simpson_3_method'),

    #num differential
    path('picards_method',views.picards_method,name='picards_method'),
    path('eulers_forward_method',views.eulers_forward_method,name='eulers_forward_method'),
    path('eulers_cauchy_method',views.eulers_cauchy_method,name='eulers_cauchy_method'),
    path('individual_runge_kutta_methods',views.individual_runge_kutta_methods,name='individual_runge_kutta_methods'),
    path('all_runge_kutta_methods',views.all_runge_kutta_methods,name='all_runge_kutta_methods'),
    
    path('adams_bashforth_method',views.adams_bashforth_method,name='adams_bashforth_method'),
    path('adams_moulton_method',views.adams_moulton_method,name='adams_moulton_method'),
    path('milve_adams_method',views.milve_adams_method,name='milve_adams_method'),
    path('milve_simpson_method',views.milve_simpson_method,name='milve_simpson_method'),

    path('adams_bashforth_pc_method',views.adams_bashforth_pc_method,name='adams_bashforth_pc_method'),
    path('milve_adams_pc_method',views.milve_adams_pc_method,name='milve_adams_pc_method'),
   
]