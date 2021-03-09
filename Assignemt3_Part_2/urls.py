"""Assignemt3_Part_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
#from People import views as People
#from People.views import PeopleCreateView, PeopleEditView, PeopleDetailView, PeopleListView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('', PeopleListView.as_view(template_name='people/people_list.html'), name='list'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # 'urls' file from the users app
    path('users/', include('django.contrib.auth.urls')),
    #path('roledex/', include('People.urls')),
    path('Selection/', include('Selection.urls')),
    path('Type/', include('Type.urls')),
    path('Roledex/', include('People.urls')),
    #path('people_list/', People.people_list, name='people_list'),
    #path('people/<int:pk>/view/', People.people_detail, name='people_view'),
    #path('new/', PeopleCreateView.as_view(), name='people_new'),
    #path('people/<int:pk>/delete/', People.people_delete, name='people_delete'),
    #path('<int:pk>/edit/',
    #     PeopleEditView.as_view(), name='people_edit'),
    #path('<int:pk>/',
     #    PeopleDetailView.as_view(), name='people_detail'),
    #path('', PeopleListView.as_view(), name='people_list'),
]
