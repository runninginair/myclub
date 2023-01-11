from django.urls import path
from . import views

urlpatterns = [
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hypen-and_underscore_stuff
    # UUID: Universally Unique Identifier
    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues', views.list_venues, name='list-venues'),
    path('show_venue/<venue_id>', views.show_venue, name="show-venue"),

]
