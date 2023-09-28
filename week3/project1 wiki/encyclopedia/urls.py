from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("new/", views.new_page, name="new_page"),
    path("edit/", views.edit, name="edit"),
    path("save_page/", views.save_page, name="save_page"),
    path("random_page/", views.random_page, name="random_page"),
]
