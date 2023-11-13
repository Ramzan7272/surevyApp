from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start, name='start'),
    path('questions/<int:pk>/<int:ans_pk>/', views.questions, name='questions'),
    path('result/<int:pk>/', views.result, name='result'),
    path('stats/', views.stats, name='stats')
]
