from django.urls import path
from app3.views import *
app3 = 'everything'
urlpatterns = [
    path('fiveth/',fiveth,name='fiveth'),
    path('sixth/',sixth,name='sixth'),
    path('demon/',demon,name='demon'),
]