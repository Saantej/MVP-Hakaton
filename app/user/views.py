from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages

from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from user.serializers import UserLoginSerializer
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        sr = UserLoginSerializer(data=request.POST)
        if sr.is_valid():
            email = sr.validated_data['email']
            password = sr.validated_data['password']
            user = auth.authenticate(email=email, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
            else:
                form = UserLoginForm(request.POST)
        else:
            form = UserLoginForm(request.POST)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


def profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserProfileForm(instance=user)


    context = {
        'form': form, 'title': 'Профиль',

    }
    return render(request, 'user/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index"))