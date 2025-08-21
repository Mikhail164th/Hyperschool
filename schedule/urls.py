from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("main/", views.search_view, name="search"),
    path("course_details/<int:pk>", views.CourseDetailView.as_view(), name="course_detail"),
    path("teacher_details/<int:pk>", views.TeacherDetailView.as_view(), name="teacher_detail"),
    path("add_course/",views.ApplyCourseView.as_view(), name="add_course"),

    ]