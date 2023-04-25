from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('', myapp),
    path('Book/' , post_Book),
    path('update-Book/<int:id>', update_Book),
    path('delete-Book/<int:id>', delete_Book),  #delete_Book
   
]
