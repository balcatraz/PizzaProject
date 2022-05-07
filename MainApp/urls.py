from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pizzas", views.pizzas, name="pizzas"),
    path("pizza/<int:pizza_id>/", views.pizza, name="pizza"),
    path("pizza/<int:pizza_id>/new_comment", views.new_comment, name="new_comment"),
    path("pizza/comments/<int:comment_id>/", views.edit_comment, name="edit_comment"),
    path("admin/", admin.site.urls),
]
