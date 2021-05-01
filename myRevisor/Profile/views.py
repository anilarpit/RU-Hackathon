from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm


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
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
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