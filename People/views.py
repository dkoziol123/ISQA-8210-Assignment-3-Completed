from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import People
from django.urls import reverse_lazy

class PeopleListView(LoginRequiredMixin, ListView):
    model = People
    template_name = 'people_list.html'

class PeopleDetailView(LoginRequiredMixin, DetailView):
    model = People
    template_name = 'people_detail.html'
    login_url = 'login'

class PeopleUpdateView(LoginRequiredMixin, UpdateView):
    model = People
    fields = ('name', 'phone', 'email', )
    template_name = 'people_edit.html'

class PeopleDeleteView(LoginRequiredMixin, DeleteView):
    model = People
    template_name = 'people_delete.html'
    success_url = reverse_lazy('people_list')

class PeopleCreateView(LoginRequiredMixin, CreateView):
    model = People
    template_name = 'people_new.html'
    fields = ('name', 'phone', 'email', )
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


