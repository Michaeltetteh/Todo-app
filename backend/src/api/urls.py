from django.urls import path
from .views import (
    todo_list,
    create,
    delete
)

app_name = "api"

api_urls = [
    path('show/',todo_list, name="list-view"),
    path('create/',create, name="create-view"),
    path('delete/<int:pk>/',delete, name="delete-view"),
]
