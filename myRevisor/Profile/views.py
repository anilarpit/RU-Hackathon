from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login_in(request):
    print('ok')
    if request.user.is_authenticated:
        return render(request, 'profile/already_login.html', {'user':request.user})
    
    else:
        print('ye')
        form = AuthenticationForm(request.POST or None)
        if form.is_valid():
            print('123434')
            user = form.get_user()
            print(user.username)
            login(request, user)
            return redirect('notes')
        else:
            print('nani')
        context = {
            'my_form' : form,
        }

        return render(request, 'profiles/login_in.html', context)


def login_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def register(request):
    user_form = UserCreationForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)

    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        profile = profile_form.save()
        profile.user = user
        profile.save()
        return redirect('notes')
    
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    return render(request, 'profiles/register.html', context)


#@transaction.atomic
@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('done')
            return redirect('notes')
            #user_form = UserForm(instance=request.user)
            #profile_form = ProfileForm(instance=request.user.profile)
        else:
            print(user_form.errors)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'profiles/profile.html', context)