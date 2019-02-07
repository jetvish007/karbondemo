from django.shortcuts import render
from django.http import HttpResponse
from user_registration.models import GreenUser, UsageDetails
from user_registration.forms import GreenUserForm
from user_registration.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    green_form = GreenUserForm()
    my_dict = {'insert_me': "Registration!!!"}
    return render(request, 'user_registration/index.html', {'form': green_form})

def home(request):
    my_dict = {'insert_me': "Registration!!!"}
    return render(request, 'user_registration/home.html', my_dict)


def welcome(request):
    return render(request, 'user_registration/welcome.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request, 'user_registration/welcome.html',{})

            else:
                return HttpResponse("Account not Active!!!")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login Details")

    else:
        return render(request, 'user_registration/login.html',{})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        green_form = GreenUserForm(data=request.POST)

        if user_form.is_valid() and green_form.is_valid():
            user1 = user_form.save()
            user1.set_password(user1.password)
            user1.save()

            details = green_form.save(commit=False)
            details.user = user1

            details.instrument_purchase = request.POST.get("instrument_purchase")
            details.house_no = request.POST.get("house_no")
            details.address_line1 = request.POST.get("address_line1")
            details.address_line2 = request.POST.get("address_line2")
            details.telephone = request.POST.get("telephone")
            details.zip_code = request.POST.get("zip_code")
            details.state = request.POST.get("state")
            details.country = request.POST.get("country")

            details.save()
            registered = True

        else:
            print(user_form.errors, green_form.errors)
    else:
        user_form = UserForm()
        green_form = GreenUserForm()

    return render(request, 'user_registration/registration.html', {'registered': registered, 'user_form': user_form, 'green_form': green_form})
