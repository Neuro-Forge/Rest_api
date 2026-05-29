from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeForwardView.as_view(), name='employe_home'),
    # path('<int:id>/', views.EmployeDetailView.as_view(), name='employe_detail'),
]


