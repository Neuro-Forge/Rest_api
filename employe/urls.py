from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeForwardView.as_view(), name='employe_home'),
]


