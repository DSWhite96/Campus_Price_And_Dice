from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib import messages
from users.admin import UserCreationForm, UserChangeForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

def edit_profile(request):
    context = {}
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
           
        return HttpResponseRedirect(reverse('campus:user_profile'))
    else:
        form = UserChangeForm(instance=request.user)
        context['form'] = form

        return render(request, 'users/edit-profile.html', context)

def change_password(request):
    context = {}

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            
            messages.success(request, f'Your password was successfully changed!')
            return HttpResponseRedirect(reverse('campus:user_profile'))
        else:
            context['form'] = form
          
    else:
        form = PasswordChangeForm(request.user)
        context['form'] = form
        return render(request, 'users/change-password.html', context)

    return render(request, 'users/change-password.html', context)