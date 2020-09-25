from django.urls import path

from core.views import Home, About, Services, Contact, Portfolio

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('services/', Services.as_view(), name='services'),
    path('contact/', Contact.as_view(), name='contact'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
]
