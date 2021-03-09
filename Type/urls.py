from django.urls import path
from . import views
from .views import (
    TypeListView,
    TypeUpdateView,
    TypeDetailView,
    TypeDeleteView,
    TypeCreateView,

)


urlpatterns = [

    path('<int:pk>/edit/',
         TypeUpdateView.as_view(), name='type_edit'),
    path('<int:pk>/',
         TypeDetailView.as_view(), name='type_detail'),
    path('<int:pk>/delete/',
         TypeDeleteView.as_view(), name='type_delete'),
    path('new/', TypeCreateView.as_view(), name='type_new'),
    path('', TypeListView.as_view(), name='type_list'),


]

