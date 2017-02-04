from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.shortcuts import render
# import reportlab
from .models import *
# Create your views here.

# from reportlab.pdfgen import canvas
from django.http import HttpResponse



def index(request):
    return render(request, 'student/index.html')

def pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)


    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    students = student_information.objects.get()
    p.drawString(100, 100, students.student_name)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def logout_user(request):
     logout(request)
     form = UserForm(request.POST or None)
     context = {
         "form": form,
     }
     return render(request, 'student/login.html', context)



def login_user(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             # albums = Album.objects.filter(user=request.user)
    #             return render(request, 'student/index.html')
    #         else:
    #             return render(request, 'student/login.html', {'error_message': 'Your account has been disabled'})
    #     else:
    #         return render(request, 'student/login.html', {'error_message': 'Invalid login'})
    return render(request, 'student/index.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                return render(request, 'student/index.html')
    context = {
        "form": form,
    }
    return render(request, 'student/register.html',context)
