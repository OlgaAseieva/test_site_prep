from django.shortcuts import render, HttpResponse, redirect
from base.models import UserReservation

# Create your views here.
def manager (request):
    return HttpResponse('Manager')

def menu (request):
    pass

def event(request):
    pass

def reserve_list(request):
    lst = UserReservation.objects.filter(in_processed=False)
    return render(request, 'reserve_list.html', context={'lst': lst, })

def update_reserve(request, pk):
    UserReservation.objects.filter(pk=pk).update(in_processed=True)
    return redirect('manager:reserve_list')
