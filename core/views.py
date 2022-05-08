from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormMixin

from core.forms import MsgForm


class Home(TemplateView):
    template_name = 'core/index.html'


# class PortfolioDetail(TemplateView):
#     template_name = 'core/index.html'


class About(TemplateView):
    template_name = 'core/about.html'


class Contact(FormView):
    template_name = 'core/contact.html'
    form_class = MsgForm

    def get_success_url(self):
        messages.success(self.request, 'Message Successfully sent.')
        return reverse_lazy('core:contact')

    def form_valid(self, form):

        mail = form.cleaned_data['email']
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        body = f"{form.cleaned_data['name']},\n\n {mail} \n\n {form.cleaned_data['message']}"

        # ctx = {}
        # body = render_to_string(
        #     'email/mail.txt',
        #     ctx
        # )

        email = EmailMessage(
            subject,
            body,
            to=['dozie.steve@gmail.com'], from_email=mail
        )
        email.send()

        return super().form_valid(form)


class Portfolio(TemplateView):
    template_name = 'core/portfolio.html'


class Services(TemplateView):
    template_name = 'core/services.html'
