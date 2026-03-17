from django.urls import path
from asosiy import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('subject/<int:pk>/', views.subject_detail, name='subject_detail')
]