from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('class/<int:class_id>/students/', views.student_list, name='student_list'),
    path('student/<int:student_id>/give-merit/', views.give_merit, name='give_merit'),
    path('student/<int:student_id>/give-behavior-points/', views.give_behavior_points, name='give_behavior_points'),
]

