from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from . import models
from django.views import generic
from django.contrib.auth.views import LoginView


def search_view(request):
    form = forms.SearchForm(request.GET or None)
    number_of_courses = models.Course.objects.count()
    context = {"form": form, "number_of_courses": f"{number_of_courses} courses"}
    if form.is_valid():
        context["searched"] = models.Course.objects.filter(title__icontains=form.cleaned_data['q'])
        return render(request,'schedule/base.html', context)
    else:
        context["searched"] = models.Course.objects.all()
        return render(request,'schedule/base.html', context)


class CourseDetailView(generic.DetailView):
    model = models.Course
    template_name = "schedule/course_details.html"
    context_object_name = "course"


class TeacherDetailView(generic.DetailView):
    model = models.Teacher
    template_name = "schedule/teacher_details.html"
    context_object_name = "teacher"


class ApplyCourseView(generic.View):
    apply_form = forms.ApplyCourseForm
    template_name = "schedule/add_course.html"

    def get(self, request):
        return render(request= self.request, template_name=self.template_name, context={"form": self.apply_form})

    def post(self, request):
        new_listener = self.apply_form(request.POST)
        if new_listener.is_valid():
            new_listener.save()
        return HttpResponseRedirect("/schedule/add_course/")


class MySignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = "/schedule/main/"
    template_name = "schedule/signup.html"


class MyLoginView(LoginView):
    success_url = "main/"
    redirect_authenticated_user = True
    template_name = "schedule/login.html"