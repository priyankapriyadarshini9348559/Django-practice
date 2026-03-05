from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# CREATE
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})


# READ
def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, "add_student.html", {"form": form})


# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')