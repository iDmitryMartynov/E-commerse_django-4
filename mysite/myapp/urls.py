from django.urls import path
from myapp.views import index, contacts

urlpatterns = [
    #http://127.0.0.1:8000/myapp/
    path('hello/', index),
    #http://127.0.0.1:8000/myapp/hello
    
    #http://127.0.0.1:8000/myapp/
    path('contacts/', contacts)
    #http://127.0.0.1:8000/myapp/contacts
    ]