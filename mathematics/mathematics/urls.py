
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('core.urls')),
    path("algebra",include('algebra.urls')),
    path("calculus",include('calculus.urls')),
    path("numerical_analysis",include('numerical_analysis.urls')),
]
