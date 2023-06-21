from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User
from .forms import AccountantSignUpForm, MinisterSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import accountant_required,minister_required


class Home:
    def home(request):
        return render(request='users/index.html')
    
# Create your views here.
class AccountantSignUpForm(CreateView):
    model = User
    form_class = AccountantSignUpForm
    template_name = 'users/accountant_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'accountant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accountant-home')


class MinisterSignUpForm(CreateView):
    model = User
    form_class = MinisterSignUpForm
    template_name = 'users/minister_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'minister'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('minister-home')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_accountant:
                return reverse('accountant-home')
            elif user.is_minister:
                return reverse('minister-home')
        else:
            return reverse('login')


@login_required
@accountant_required
def accountant_home(request):
    
    return render(request, 'users/accountant_home.html')


@login_required
@minister_required
def minister_home(request):
    
    return render(request, 'users/minister_home.html')

