from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api overview"),
    path('add-task', views.create_task, name="create task"),
    path("update-task/<str:pk>/", views.update_task, name="update task"),
    path('del-task/<str:pk>/', views.delete_task, name="delete task"),
    path('get-task', views.get_task, name="get task"),
]
