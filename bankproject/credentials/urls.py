from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('adddetails/', views.adddetails, name='adddetails'),
    path('addbridge/', views.addbridge, name='addbridge'),
    path('dependentfield/<int:id>/', views.dependentfield, name='dependentfield'),
]
