from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User


from posts.models import Post
from .forms import UserForm

def register_view(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'])
            registered = True
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'accounts/register.html', {'form': user_form, 'registered':registered})


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return HttpResponseRedirect(reverse('index'))

        else:
            return HttpResponse('Invalid login details!')

    return render(request, 'accounts/login.html', {})
        

@login_required
def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))


def dashboard_view(request, id):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(uploader__id=id)

    return render(request, 'accounts/dashboard.html', {'posts':posts, 'user':user})

