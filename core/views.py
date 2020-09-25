from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'core/index.html'


# class PortfolioDetail(TemplateView):
#     template_name = 'core/index.html'


class About(TemplateView):
    template_name = 'core/about.html'


class Contact(TemplateView):
    template_name = 'core/contact.html'


class Portfolio(TemplateView):
    template_name = 'core/portfolio.html'


class Services(TemplateView):
    template_name = 'core/services.html'
