from django.shortcuts import render, redirect 
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('ursername')
          messages.success(request, f'Your Account has been Created, { username }! Now you can Log In!')
          return redirect("login")
    else:
        form = UserRegisterForm()
    #form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# messages.debug, info, success, warning, error