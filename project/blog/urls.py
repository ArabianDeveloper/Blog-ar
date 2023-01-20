from django.urls import path
from . import views


urlpatterns = [
    path('' , views.index , name = "index"),
    path('about' , views.about , name = "about"),
    path('detail/<int:id>' , views.detail , name = "detail"),
    path('new' , views.N_post , name = "new"),
    path('delete/<int:id>' , views.D_post , name = "delete"),
    path('update/<int:id>' , views.U_post , name = "update"),
]
