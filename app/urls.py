from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor/', views.doctor, name='doctor'),
    path('labmember/', views.labmember, name='labmember'),
    path('patient/', views.patient, name='patient'),
    path('patient_home/', views.patient_home, name='patient_home'),
    path('base/', views.base, name='base'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register')
]