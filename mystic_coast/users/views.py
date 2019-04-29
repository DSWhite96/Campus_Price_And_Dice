from django.shortcuts import render, redirect
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

def load_profile(request):
    form = UserChangeForm(instance=request.user)
    context = {
        'form': form
    }

    return render(request, 'users/edit-profile.html', context)
