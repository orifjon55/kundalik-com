from django.urls import path
from .import views

urlpatterns = [
    path("",views.PrincipalView.as_view(), name='principal_url'),
    path('search/',views.SearchView.as_view(), name='principal_search_url')
]