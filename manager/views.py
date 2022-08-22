from django.shortcuts import render, HttpResponse, redirect
from base.models import UserReservation
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def is_manager(user):
    return user.groups.filter(name='manager').exists()

@login_required(login_url='/login/')
def manager(request):
    return HttpResponse('Manager')


def menu(request):
    pass


def event(request):
    pass


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reserve_list(request):
    lst = UserReservation.objects.filter(in_processed=False)
    return render(request, 'reserve_list.html', context={'lst': lst})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reserve(request, pk):
    UserReservation.objects.filter(pk=pk).update(in_processed=True)
    return redirect('manager:reserve_list')
