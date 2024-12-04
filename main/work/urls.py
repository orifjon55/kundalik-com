from django.urls import path
from .import views

urlpatterns = [
    path('',views.WorkView.as_view(), name='work_url'),
    path('status/',views.WorkStatus.as_view(), name='work_status_url'),
    path('search/',views.WorkSearch.as_view(), name='search_url')
]