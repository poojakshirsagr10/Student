from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required(login_url='login_url')
def create(request):
    template_name="crud_app/create.html"
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("student added")
    context={"form": form}
    return render(request, template_name, context)
@login_required(login_url='login_url')
def show(request):
    template_name='crud_app/show.html'
    all_student = Student.objects.all()

    context={"all_student":all_student}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def update(request,pk):
    obj=Student.objects.get(id=pk)
    form = StudentForm(instance=obj)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name="crud_app/create.html"
    context = {"form": form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def delete(request,pk):
    obj = Student.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request,template_name="crud_app/delete.html")
