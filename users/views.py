from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CutstomUserCreationForm


class SignUpPageView(CreateView):
    form_class = CutstomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
