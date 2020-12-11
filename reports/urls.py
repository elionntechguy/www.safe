from django.urls import path
from . import views
from .views import (
    RaportetCreateView
)

urlpatterns = [
    path('', views.index, name="wwwsafe-home"),
    path('support/', views.support, name="wwwsafe-support"),
    path('contact/', views.contact, name="wwwsafe-contact"),
    path('about/', views.about, name="wwwsafe-about"),
    path('report/', views.RaportetCreateView.as_view(), name="wwwsafe-report"),
]