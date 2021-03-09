from django.urls import path
from . import views
from .views import (
    SelectionListView,
    SelectionUpdateView,
    SelectionDetailView,
    SelectionDeleteView,
    SelectionCreateView,

)


urlpatterns = [

    path('<int:pk>/edit/',
         SelectionUpdateView.as_view(), name='selection_edit'),
    path('<int:pk>/',
         SelectionDetailView.as_view(), name='selection_detail'),
    path('<int:pk>/delete/',
         SelectionDeleteView.as_view(), name='selection_delete'),
    path('new/', SelectionCreateView.as_view(), name='selection_new'),
    path('', SelectionListView.as_view(), name='selection_list'),


]

