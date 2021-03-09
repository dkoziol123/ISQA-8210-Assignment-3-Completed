from django.urls import path
from . import views
from .views import (
    PeopleListView,
    PeopleUpdateView,
    PeopleDetailView,
    PeopleDeleteView,
    PeopleCreateView,

)


urlpatterns = [

    path('<int:pk>/edit/',
         PeopleUpdateView.as_view(), name='people_edit'),
    path('<int:pk>/',
         PeopleDetailView.as_view(), name='people_detail'),
    path('<int:pk>/delete/',
         PeopleDeleteView.as_view(), name='people_delete'),
    path('new/', PeopleCreateView.as_view(), name='people_new'),
    path('', PeopleListView.as_view(), name='people_list'),


]

