from django.shortcuts import render,redirect
from django.contrib.auth import logout
from core import models, forms
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User

def home(request):
    return render(request,'home_core.html',)

def register(request):
    if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')

                if User.objects.filter(username=email).exists():
                    messages.error(request, 'A user with this Email already exists.')
                    return redirect('login')
                
                try:
                    user = form.save(commit=False)
                    user.username = email  # Using Email as the username
                    user.save()
                except Exception as e:
                    messages.error(request, f'An error occurred while trying to create your account.[{e}]')
                    return redirect('register')
                
                messages.success(request, 'Account created successfully.')
                login(request, user)
                return redirect('home')
            
            # else:
            #     for field, errors in form.errors.items():
            #         for error in errors:
            #             messages.error(request, f"{error}")# Display form errors as messages
            return render(request, 'login_register.html', {'register_form': form})
    else:
        form= forms.RegisterForm()
        return render(request, 'login_register.html', {'register_form': form})
        
def log_in(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid login credentials. Please try again.")

        return render(request, 'login_register.html', {'login_form': form})

    else:
        form = forms.LoginForm()

    return render(request, 'login_register.html', {'login_form': form})
 

def log_out(request):
    messages.success(request,"Logged out successfully!")
    logout(request)
    return render(request,'home_core.html')

def about(request): 
    return render(request,'about.html')

def feedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        feedback_1=request.POST.get('feedback1')
        feedback_2=request.POST.get('feedback2')
        first_impression=request.POST.get('firstimpression')
        improve_experience=request.POST.get('improveexperience')
        updated_on=request.POST.get('updated_on') 
        links=request.POST.get('links')
        message=request.POST.get('message')
        models.Feedback.objects.create(
            name=name,
            email=email,
            feedback1=feedback_1,
            feedback2=feedback_2,
            firstimpression=first_impression,
            improveexperience=improve_experience,
            updated_on=updated_on,
            links=links,
            message=message,
        )
        messages.success(request,'Thank you for your feedback.')
        return render(request,'home_core.html')
    return render(request,'feedback.html')

def report(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        links=request.POST.get('links')
        message=request.POST.get('message')
        reportfile=request.FILES.get('reportfile')
        date=request.POST.get('date')
        models.Report.objects.create(
            name=name,
            email=email,
            links=links,
            message=message,
            date=date,
            reportfile=reportfile,
        )
        messages.success(request,'Report successfully sent.')
        return render(request,'home_core.html')
    return render(request,'report.html')

def credits(request):
    if request.user.is_authenticated:
        return render(request,'credit.html',{'allcredit':models.Credit.objects.all()})
    else:
        messages.info(request,"Login required.")
        return render(request,'login.html')

def commingsoon(request):
    messages.error(request,"Access denied!")
    return render(request,'home_core.html')

def finance(request):
    messages.info(request,"Clicking below will take you to Fimac-Finance* website. (*in development)")
    return render(request,'finance_redirect.html',{'link':'https://fimac.pythonanywhere.com/'})



