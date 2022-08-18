from django.shortcuts import render, HttpResponse

# Create your views here.
def client_general (request):
    return HttpResponse(f'Client with ')

def client (request, client_number):
    return HttpResponse(f'Client with ID {client_number}')
