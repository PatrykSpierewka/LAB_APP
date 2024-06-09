from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, TestPackageForm # AddResult
from django.contrib.auth import authenticate, login
from .models import Patients

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            elif user is not None and user.is_labmember:
                login(request, user)
                return redirect('labmember')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def home(request):
    return render(request, 'homepage.html')

def doctor(request):
    return render(request, 'doctor.html')

def labmember(request):
    return render(request, 'labmember.html')

def base(request):
    return render(request, 'base.html')

def patient_home(request):
    return render(request, 'patient_home.html')

def patient(request):
    if request.method == 'POST':
        form = TestPackageForm(request.POST)
        if form.is_valid():
            # Obsługa zapisu wybranego pakietu badań do bazy danych
            form.save()
            # Przekierowanie do innej strony po zapisie
            return redirect('patient.html')
    else:
        form = TestPackageForm()
    return render(request, 'patient.html', {'form': form})

def addresult(request):
    print("Widok wywołany")  # Debug: Sprawdź, czy widok jest wywoływany
    if request.method == "POST":
        pacjenci = health_id = Patients.objects.filter(name="Marek").values_list("health_id", flat=True).first()
        print(pacjenci)
        print("Wysłano:", request.POST)  # Debug: Sprawdź dane POST
    #     form = AddResult(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print("Formularz zapisany")  # Debug: Sprawdź, czy formularz został zapisany
    #         return redirect('labmember')  # Upewnij się, że ten URL istnieje
    #     else:
    #         print("Formularz nie jest poprawny", form.errors)  # Debug: Wypisz błędy formularza
    # else:
    #     form = AddResult()
    return render(request, 'addresult.html') #{'form': form}