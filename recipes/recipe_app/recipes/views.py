from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Recipe

def home(request):
    return render(request, 'home.html')
def register(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user and generates the password
            messages.success(request, f'Your account has been created! Your password is: {user.password}')  # Inform user of their password
            login(request, user)  # Log the user in
            return redirect('recipe_list')  # Redirect after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user)  
    return render(request, 'recipe_list.html', {'recipes': recipes})