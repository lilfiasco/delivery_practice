# Python
from typing import Any, Dict
from django import http

#Django
from django.shortcuts import (
    render, 
    redirect,
    resolve_url
)
import sys  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    View, 
    DetailView
)
from django.views.generic.edit import UpdateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView
from django.utils.decorators import method_decorator
from rest_framework.generics import CreateAPIView

#Local
from auths import (
    forms,
    models,
)


class UserRegisrtrationView(CreateView):
    """
    RegistrationView for custom user.
    """

    form_class = forms.CustomUserForm
    success_url = reverse_lazy('registraion')
    template_name = 'auths/registration.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print('FFFFFFFFF: ', context)
        return context
    
    def form_valid(self, form):
        custom_user = form.save(commit=False)
        custom_user.password = make_password(form.cleaned_data['password'])
        custom_user.save()
        # return reverse_lazy('index')
        return render(self.request, 'auths/registration_success.html')


class CoworkerRegisrtrationView(CreateView):
    """
    RegistrationView for custom user.
    """

    form_class = forms.CoworkerForm
    success_url = reverse_lazy('registraion_coworker')
    template_name = 'auths/registration_coworker.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print('FFFFрFFFFF: ', context)
        return context
    
    def form_valid(self, form):
        custom_user = form.save(commit=False)
        custom_user.password = make_password(form.cleaned_data['password'])
        custom_user.save()
        # return reverse_lazy('index')
        return render(self.request, 'auths/registration_success.html')



class CustomLoginView(LoginView):
    template_name = 'auths/login.html'
    # form_class = forms.CustomLoginForm
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        return super().form_invalid(form)
    
    def get_success_url(self):
        return resolve_url('index')


class CustomLogoutView(View):
    """LogoutView."""

    def get(self, request) -> HttpResponse:
        if request.user:
            logout(request)
        
        return redirect('index')
    
    
@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = models.CustomUser
    template_name = 'auths/profile.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        user = get_object_or_404(models.CustomUser, pk=self.kwargs['pk'])
        return user

        
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.CustomUser
    template_name = 'auths/update_profile.html'
    fields = ['first_name', 'last_name', 'phone_number', 'birth_date']

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        phone_number = form.cleaned_data.get('phone_number')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')

        if len(phone_number) != 12:
            form.add_error('phone_number', 'Недопустимый формат данных номера телефона')

        if len(first_name) < 2:
            form.add_error('first_name', 'Недопустимый формат личных данных')

        if len(last_name) < 2:
            form.add_error('last_name', 'Недопустимый формат личных данных')

        messages.success(self.request, 'Профиль успешно обновлен!')
        return super().form_valid(form)


class CustomUserPasswordChange(View):
    template_name = "auths/change_password.html"
    def get(self, request, *args, **kwargs):
        context = {"user": request.user}
        
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        current_password = request.POST.get("old_pass")
        if current_password:
            if request.user.check_password(current_password):
                new_password = request.POST.get('new_pass', '').strip()
                confirm_password = request.POST.get('confirm_new_pass', '').strip()
                if new_password and confirm_password and new_password == confirm_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    return redirect('logout')
                else:
                    messag = 'Поля «Новый пароль» и «Подтверждение пароля» должны совпадать!'
                    messages = ""
                    context = {
                        
                        'messag': messag,
                        'messages':messages,
                    }
                    return render(request, 'main/profile.html', context)
            else:
                messag = 'Текущий пароль неверный!'
                messages = ""
                context = {
                    
                    'messag': messag,
                    'messages':messages,
                }
                return render(request, 'auths/change_profile', context)
            



from .serializers import OrderSerializer

class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.validated_data['customer'] = self.request.user

        total_price = 0
        serializer.validated_data['total_price'] = total_price

        serializer.save()
