from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Type
from django.urls import reverse_lazy

class TypeListView(LoginRequiredMixin, ListView):
    model = Type
    template_name = 'type_list.html'

class TypeDetailView(LoginRequiredMixin, DetailView):
    model = Type
    template_name = 'type_detail.html'
    login_url = 'login'

class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    fields = ('Recreation_Name', 'Recreation_Type_Indoor', 'Recreation_Type_Outdoor', 'Public', 'Private',)
    template_name = 'type_edit.html'

class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'type_delete.html'
    success_url = reverse_lazy('type_list')

class TypeCreateView(LoginRequiredMixin, CreateView):
    model = Type
    template_name = 'type_new.html'
    fields = ('Recreation_Name', 'Recreation_Type_Indoor', 'Recreation_Type_Outdoor', 'Public','Private',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


