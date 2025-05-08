from django.shortcuts import render,redirect
from django.contrib.auth import authenticat,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def connexion (request):
  if request.method == 'POST' :
    username = request.POST['username']
    password = request.POST['password']
    user = authenticat(username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('accueil')
    else :
      return render(request,'login.html',{'erreur':'Identifiants incorrect'})
    return render(request,'login.html')

def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'register.html', {'erreur': 'Les mots de passe ne correspondent pas'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'erreur': 'Ce nom d’utilisateur existe déjà'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('login')

    return render(request, '/register.html')

def deconnexion(request):
  logout(request)
  return redirect('login')

@login_required(login_url='login')
def accueil(request):
    return render(request, 'comptes/accueil.html')