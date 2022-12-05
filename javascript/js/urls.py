from django.urls import path
from .import views

urlpatterns=[
    path('palindrome',views.palindrome),
    path('element',views.element),
    path('element_find',views.element_find),
    path('largest',views.largest),
    path('second_largest',views.second_largest)
]