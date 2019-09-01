from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):##
    a=2
    context = {}
    context.update({'a': a})
    return render(request, 'index.html', context)

def login(request): # Вход в приложение
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active: # Проверяем юзера на активность
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)# логинимся в систему
            try:
                next = request.GET['next']
                return HttpResponseRedirect(next)
            except:
                # Перенаправление на "правильную" страницу
                a=1
                return HttpResponseRedirect('/applicants/profile/%s/' % user.pk)
        else:
            # Отображение страницы с ошибкой
            err = 'Неправильный логин или пароль'
            return render(request, 'login.html', {'usererror': err})
    else:
        return render(request, 'login.html')

def logout(request): #
    auth.logout(request)
    return HttpResponseRedirect('/')

def registration(request): #
    context={}
    err = ''
    if request.method == 'POST':
        login = request.POST.get('login')
        name = request.POST.get('name')
        password = request.POST.get('pass')
        pass_again = request.POST.get('pass_again')
        if password != pass_again:
            err = 'Пароли не воспадают'
        try:
            user = User.objects.get(email=login)
            err = 'Пользователь с таким email уже существует'
        except:
            user = User.objects.create(username=name,first_name=name, email=login,password=password)
            user.save()
            #request.user = user
            auth.login(request, user ,backend='django.contrib.auth.backends.ModelBackend')
        if not err:
            return HttpResponseRedirect('/applicants/profile/%s/' % user.pk)
        else:
            context.update({'usererror': err})
    return render(request, 'registration.html', context=context)