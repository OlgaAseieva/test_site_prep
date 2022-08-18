from django.contrib import admin
from .models import Category, Menu, Event, Galery, WhyUs, AboutUs, UserReservation #, Spesial
from .models import Category, Menu, Event, AboutUs, Galery, WhyUs, UserReservation
from django.contrib import admin

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('name', ), }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ('date_ev', )

#admin.site.register(Category)
#admin.site.register(Menu)
admin.site.register(AboutUs)
#admin.site.register(Event)
admin.site.register(Galery)
admin.site.register(WhyUs)
#admin.site.register(Spesial)
admin.site.register(UserReservation)
