from django.shortcuts import render
from .forms import UserCreateForm, CategoriaInteresForm
from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html',
            {'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], email=request.POST['email'], role=request.POST['role'], age=request.POST['age'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('category',request.POST['username'])
            except IntegrityError:
                return render(request, 'signupaccount.html',
                {'form':UserCreateForm,
                'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'signupaccount.html',
            {'form':UserCreateForm, 'error':'Passwords do not match'})
        
    

@login_required       
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
    if user is None:
        return render(request,'loginaccount.html',{'form': AuthenticationForm(),'error': 'username and password do not match'})
    else:
        login(request,user)
    return redirect('home')

@login_required
def InterestCategories(request,name):
    if request.method == 'POST':
        form = CategoriaInteresForm(request.POST)
        if form.is_valid():
            categorias_interes = form.cleaned_data.get('CategoriaInteres')
            user = User.objects.get(username = name)
            user.CategoriaInteres.extend(categorias_interes) 
            user.save()
            return redirect('home')
    else:
        form = CategoriaInteresForm()

    return render(request, 'categoriaInteres.html', {'form': form})