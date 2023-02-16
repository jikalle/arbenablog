from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            new_user = form.save(data=request.POST)
            login(request, new_user)
            return redirect('home-index')
    else:
        form = UserCreationForm()
        
    context = {
        'form': form
    }
    return render(request, 'register/register.html', context)
