from django.shortcuts import render
from .forms import CustomUserCreateForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

class SignUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



