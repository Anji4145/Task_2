from django.urls import path
from app1.views import *
app1 = 'something'
urlpatterns =[ 
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    path('calling/',calling,name='calling'),

]