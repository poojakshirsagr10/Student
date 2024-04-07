from django.urls import path
from .views import create, show, update, delete

urlpatterns =[
    path("create/", create, name="create_url"),
    path("show/", show, name="show_url"),
    path("update/<int:pk>/", update, name="update_url"),
    path("delete/<int:pk>/", delete, name="delete_url")
]