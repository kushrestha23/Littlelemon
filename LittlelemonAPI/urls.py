from django.urls import path
from . import views

urlpatterns = [
    path("menu-items/", views.MenuItem.as_view()),
    path("api/", views.api_view, name="api_endpoint"),
    path("menu-items/<int:pk>", views.SingleMenuItem.as_view()),
]
