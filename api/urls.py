from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:id>/', views.student_views, name='student_views'),
    path('employe/', views.employe.as_view(), name='employe_list'),
    path('employe/<int:pk>/', views.employe_detail.as_view(), name='employe_detail'),
    
]

