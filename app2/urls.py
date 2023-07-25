from django.urls import path
from app2.views import *
app2 = 'Nothing'
urlpatterns = [
    path('third/',third,name='third'),
    path('fourth/',fourth,name='fourth'),
    path('illusion/',illusion,name='illusion'),
]