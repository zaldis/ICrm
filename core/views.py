from django.http import HttpResponse
from django.views.generic import FormView, TemplateView

from core.forms import LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = ...

    def get(self, *args, **kwargs) -> HttpResponse:
        return super().get(*args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     form = self.get_form()
    #     return context

    def form_valid(self, form):
        # authenticate member
        print("correct email")
        return super().form_valid(form)