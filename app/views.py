from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, TestPackageForm,User # AddResult
from django.contrib.auth import authenticate, login, logout
from .models import Patients,Tests,Results

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
                return redirect('base')
            elif user is not None and user.is_labmember:
                login(request, user)
                return redirect('base')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('base')
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

    print(f'Labmember view {request.method}')
    if request.method == "GET":
        tests=list(Tests.objects.values())
        context={}
        for idx,test in enumerate(tests):
            result_id=test['result_id_id']
            results=list(Results.objects.filter(result_id=result_id).values())
            print(f'Result {results}')
            for result in results:
                for key in result.keys():
                    test.update({key:result[key]})
                context[f'test{idx}']=test
              
        print(f'Context {context}')
        #pacjenci = Patients.objects.filter(name="Marek").values_list("health_id", flat=True).first()
    return render(request, 'labmember.html',{'tests':context})

def base(request):
    if request.user.is_authenticated:
        is_doctor = request.user.is_doctor
        is_labmember = request.user.is_labmember
        is_patient = request.user.is_patient
        print(f'Active user {is_doctor},{is_labmember},{is_patient}')
        active_user = ''
        if is_doctor==True:
            active_user='doctor'
        elif is_labmember==True:
            active_user='labmember'
        else:
            active_user='patient'

        context = {'active_user': active_user}
        return render(request, 'base.html', context)
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

def user_logout(request):
    logout(request)
    return redirect('/')

def addresult(request):
    print("Widok wywołany")  # Debug: Sprawdź, czy widok jest wywoływany
    if request.method == "POST":
        pacjenci = Patients.objects.filter(name="Marek").values_list("health_id", flat=True).first()
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

