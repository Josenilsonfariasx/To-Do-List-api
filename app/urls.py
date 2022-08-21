from django.urls import path

from app.views import TodoDetailChangeAndDelete, TodoListAndCreate

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/',TodoDetailChangeAndDelete.as_view()),
]
