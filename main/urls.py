from django.urls import path
# from main.views import index_view, about_developer
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("about/", views.about_developer, name="about"),
    path("course/<int:pk>/", views.course_detail, name="course_detail")
]