from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) #instantiate form with submitted data
        if form.is_valid(): #checks if the form is valid 
            cd = form.cleaned_data
            user = authenticate(request, #if valid, data is authenticated against the database
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active: #check if user is active
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')#response if authenticated and active
                    else:
                    return HttpResponse('Disabled account') #response if authenticated and not active
            else:
            return HttpResponse('Invalid login') #if not authenticated, raw response
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


