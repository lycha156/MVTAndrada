from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="familiares_index" ),
    path('create', views.create, name="familiares_create"),
    path('update/<int:id>', views.update, name="familiares_update"),
    path('delete/<int:id>', views.delete, name="familiares_delete"),
    path('show/<int:id>', views.show, name="familiares_show"),
]
