from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.

def index(request):
    services = Service.objects.all()[:4]
    image = AboutImage.objects.get(pk=1)
    chefs = Chef.objects.all()[:4]
    feedbacks = Testimonial.objects.all()
    if request.method == "POST":
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = ReservationForm()

    context = {
        'title': "Главная страница",
        'form': form,
        'services': services,
        'image': image,
        'chefs': chefs,
        'feedbacks': feedbacks
    }
    return render(request, 'res/index.html', context)


def about(request):
    image = AboutImage.objects.get(pk=1)
    chefs = Chef.objects.all()
    context = {
        'title': "О нас",
        'image': image,
        'chefs': chefs
    }
    return render(request, 'res/about.html', context)


def service(request):
    services = Service.objects.all()
    context = {
        'title': "Сервисы",
        'services': services,
    }
    return render(request, 'res/service.html', context)


def menu(request):
    context = {
        'title': "Меню"
    }
    return render(request, 'res/menu.html', context)


def booking(request):
    if request.method == "POST":
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = ReservationForm()
    context = {
        'title': "Забронировать стол",
        "form": form
    }
    return render(request, 'res/booking.html', context)


def team(request):
    chefs = Chef.objects.all()
    context = {
        'title': "Наша команда",
        'chefs': chefs,
    }
    return render(request, 'res/team.html', context)


def testimonial(request):
    feedbacks = Testimonial.objects.all()
    context = {
        'title': "Отзывы",
        'feedbacks': feedbacks
    }
    return render(request, 'res/testimonial.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = ContactForm()

    context = {
        'title': "Контакты",
        'form': form
    }
    return render(request, 'res/contact.html', context)



def leave_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FeedbackForm()
    context = {
        'title': "Оставить отзыв",
        'form': form
    }
    return render(request, 'res/leave_feedback.html', context)
