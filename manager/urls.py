from django.urls import path
from .views import manager, menu, event, reserve_list, update_reserve

app_name ='manager'

urlpatterns = [
    path('', manager),
    path('menu/', menu),
    path('event/', event),
    path('reserve/', reserve_list, name = 'reserve_list'),
    path('reserve/update/<int:pk>/', update_reserve, name= 'update_reserve')

]
