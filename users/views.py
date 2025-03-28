from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from .models import CustomUser
from .forms import CustomRegisterForm

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('users:login')

class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:user_list")

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

class UserListView(ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = CustomUser

    def get_queryset(self):
        return self.model.objects.all()


