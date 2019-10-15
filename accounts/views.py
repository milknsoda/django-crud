from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('articles:index')
    else:
        new_user = UserCreationForm()
    context = {
        'new_user': new_user
    }
    return render(request, 'accounts/signup.html', context)