from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
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
            return render(request, 'login.html', {'usererror': username})
    else:
        return render(request, 'login.html')

def logout(request): #
    auth.logout(request)
    return HttpResponseRedirect('/')