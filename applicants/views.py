from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.
def check_user_access(request, id):
    context = {}
    #TODO Дописать проверку id юзера к id документа
    if request.user.is_staff or id == str(request.user.id):
        return True
    else:
        context.update({'error': {'code': 'Ошибка доступа', 'title':'Ошибка прав доступа', 'message':'У вас нехватает прав на просмотр данной страницы'}})
        return render(request, '500.html', context=context)
@login_required(login_url='/login/')
def profile(request, id):##
    check_user_access(request, id)
    return render(request, 'index_profile.html')

@login_required(login_url='/login/')
def profile(request, id):##
    rules = check_user_access(request, id)
    if rules is not True:
        return rules
    return render(request, 'index_profile.html')

@login_required(login_url='/login/')
def profile_valid(request):##
    return HttpResponseRedirect('/applicants/profile/%s' % request.user.pk)
