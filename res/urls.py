from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('menu/', menu, name='menu'),

    path('booking/', booking, name='booking'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),
    path('leave_feedback/', leave_feedback, name='leave_feedback'),
]