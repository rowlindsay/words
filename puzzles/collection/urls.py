from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:collection_name>/puzzle', views.by_collection_date, name='puzzle_by_date')
]
