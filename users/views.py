from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'welcome {username}, youve been logged in')
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form':form})
    
    
@login_required()
def profilepage(request):
    return render(request, 'users/profile.html')