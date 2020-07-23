from django.urls import path
from . import views

urlpatterns =[
    path("", views.index ,name='index'),
    path("about/", views.about ,name='about'),
    path("tracker/", views.tracker ,name='tracker'),
    path("search", views.search ,name='search'),
    path("productview", views.productview ,name='productview'),
    path("contact", views.contact ,name='contact'),
    path("checkout", views.checkout ,name='checkout'),
]

