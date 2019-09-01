from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.
def profile(request, id):##
    return render(request, 'index_profile.html')

def profile_valid(request):##
    return HttpResponseRedirect('/applicants/profile/%s' % request.user.pk)
