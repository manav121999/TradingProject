from django.urls import path
from MainApp.views import index

urlpatterns = [
    path('',index,name='index'),   
]
