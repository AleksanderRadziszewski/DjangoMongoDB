from django.shortcuts import render
from django.views import View

from .models import Student


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "student_data.html", {"students": students})
# Create your views here.
