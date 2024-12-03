from django.urls import path
from .import views

urlpatterns = [
    path("",views.StudentView.as_view(), name='student_url'),
    path('search/',views.SearchViews.as_view(), name='student_search_url')
]