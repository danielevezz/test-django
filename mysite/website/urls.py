from django.urls import path

from . import views

urlpatterns = [
    path('', views.program, name='program'),
    path('<int:event_id>/', views.detail, name='detail'),
]
