from .views import todo_list
from django.urls import path

from app import views

urlpatterns = [
    path('', todo_list),
    path('<int:pk>/', views.todo_detail_change_and_delete)
]
