from django.contrib.auth.decorators import permission_required
from django.views.generic import (ListView,
                                  DetailView,
                                  TemplateView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from users.models import User
from users.forms import UserRegisterForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:login")

class UserListView(ListView):
    model = User
    permission_required = 'users.change_user'

@permission_required('users.change_user')
def ActivateUser(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False if user.is_active else True
    user.save()
    return redirect('users:list')