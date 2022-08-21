from django.urls import path, include
from app.views import TodoViewSet
from rest_framework import routers

route = routers.DefaultRouter()

route.register(r'todo',TodoViewSet, basename= 'todo')

urlpatterns = [
    path('', include(route.urls))
    
]
