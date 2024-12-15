from .views import GET_ALLTODO,INSERT_TODO,MANIDATA
from django.urls import path

# route

urlpatterns = [
    path('gettodo/',GET_ALLTODO,name='getalltodo'),
    path('inserttodo/',INSERT_TODO,name="inserttododata"),
    path("todo/item/<int:id>/",MANIDATA,name="deletetodo")
]


# http://localhost:8000/todoapi/inserttodo/

# python3 manage.py runserver

# http://localhost:8000
# http://127.0.0.1:8000


# JSON = javascript object notation