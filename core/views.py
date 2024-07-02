from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from core.flows.developer_request import node_runner as developer_request_node_runner
from core.services.developer_request import (
    get_active_developer_request,
    get_developer_request_by_id,
    get_passed_developer_requests,
    suggest_new_developer,
    cancel_suggested_developer,
)
from core import forms

from user.services.customer import get_customer_by_user_id
from user.services.delivery_manager import get_delivery_manager_by_user_id
from user.services.developer import get_developers_on_bench


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = get_customer_by_user_id(self.request.user.id)
        delivery_manager = get_delivery_manager_by_user_id(self.request.user.id)
        if delivery_manager:
            customer = delivery_manager.customer
            context['developers_on_bench'] = get_developers_on_bench()

        if customer:
            context['active_developer_request'] = get_active_developer_request(customer.id)
            context['passed_developer_requests'] = get_passed_developer_requests(customer.id)
        return context


class DeveloperRequestView(View):
    form_class = forms.NewDeveloperRequestForm
    success_url = reverse_lazy('core:profile')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            developer_request_node_runner.run_start_node(
                customer_id=form.cleaned_data['requested_by'].id,
                specialization=form.cleaned_data['specialization'],
                grade=form.cleaned_data['grade'],
            )
            return redirect(self.success_url)


class SuggestedDeveloperView(View):
    form_class = forms.DeveloperForm
    success_url = reverse_lazy('core:profile')

    def post(self, request: HttpRequest, developer_request_id: int, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            developer_request = get_developer_request_by_id(developer_request_id)
            suggested_developer = form.cleaned_data['developer']
            if request.GET.get('action') == 'cancel':
                cancel_suggested_developer(developer_request.id, suggested_developer.id)
            else:
                suggest_new_developer(developer_request.id, suggested_developer.id)
            return redirect(self.success_url)


class DeveloperApproveView(DetailView):
    form_class = forms.DeveloperForm
    success_url = reverse_lazy('core:profile')

    def post(self, request: HttpRequest, developer_request_id: int, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            developer_request = get_developer_request_by_id(developer_request_id)
            approved_developer = form.cleaned_data['developer']
            developer_request_node_runner.run_approve_by_customer_node(
                developer_request.id, approved_developer.id
            )
            return redirect(self.success_url)
