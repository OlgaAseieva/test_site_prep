
from django.shortcuts import render, redirect,  HttpResponse
from .forms import UserReservationForm
from .models import Category, Menu, Event, WhyUs, AboutUs, Galery

# Create your views here.
def base (request):

    if request.method == 'POST':
        reserve = UserReservationForm(request.POST)
        if reserve.is_valid():
            reserve.save()
            return redirect('/')

    # for request.GET:

    categories = Category.objects.filter(is_visible=True)
    menus = Menu.objects.filter(is_visible=True)
    specials = Menu.objects.filter(special_dish=True)
    event = Event.objects.filter(is_visible=True)
    whyus = WhyUs.objects.all()
    about = AboutUs.objects.filter(is_visible=True)
    gallerys = Galery.objects.filter(is_visible = True)
    reserve = UserReservationForm()

    data = {'categories': categories,
            'menus': menus,
            'specials': specials,
            'event': event,
            'about': about,
            'whyus': whyus,
            'gallerys': gallerys,
            'reserve_form': reserve
            }
    return render(request, 'base.html', context=data)
