from django.urls import path,include

urlpatterns = [
    path('student/',include('main.student.urls')),
    path('principal/',include('main.principal.urls')),
    path('teachers/',include('main.teachers.urls'))
]