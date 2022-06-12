from urllib.parse import quote
from django.db.models import fields
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse, request
from django.template import context
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import edit_profile_form
from django.core.files.storage import FileSystemStorage
from .models import chat, friend_list, friend_request, post, user_comment
from homepage.forms import edit_profile_form
from .models import profile
from .models import user_comment
from .forms import edit_post_form
from .models import friend_request
from .models import friend_list
from django.db.models import Sum
from django.db.models import Q
from .models import chat


def home(request):
    return render(request, "index.html")


class woman (ListView):
    model = profile
    template_name = "woman.html"
    ordering = ['-id']


class man (ListView):
    model = profile
    template_name = "man.html"
    ordering = ['-id']


class user_profile (ListView):
    model = profile
    template_name = "profile.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(user_profile, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['friend_request_list'] = friend_request.objects.all()
        context['request_count'] = friend_request.objects.filter(friend_user_name = self.request.user.username).aggregate(sum_all=Sum('request_count')).get('sum_all')
        context['friend_count'] = friend_list.objects.filter(Q(request_user_name = self.request.user.username) | Q(username = self.request.user.username)).aggregate(sum_all=Sum('friend_count')).get('sum_all')
        return context


class user_profile_view (DetailView):
    model = profile
    template_name = "user_profile.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(user_profile_view, self).get_context_data(
            *args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['friend_request_list'] = friend_request.objects.all()
        context['friend'] = friend_list.objects.all()
        return context


def about_form(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        height = request.POST['height']
        weight = request.POST['weight']
        eyes = request.POST['eyes']
        hair = request.POST['hair']
        education = request.POST['education']
        phone = request.POST['phone']
        email = request.POST['email']
        description = request.POST['description']
        gender = request.POST['gender']

        if profile.objects.filter(username=username).exists():
            messages.error(
                request, "You have already added your info.To make change go to edit profile.")
            return redirect("edit_about")
        else:
            profile_database = profile(name=name, username=username, height=height, weight=weight, eyes=eyes,
                                       hair=hair, education=education, phone=phone, email=email, description=description, gender=gender)

            profile_database.save()

            return redirect("about")


class about (ListView):
    model = profile
    username = None
    template_name = "about.html"


class user_about (DetailView):
    model = profile
    template_name = "user_about.html"


def edit_about(request):
    return render(request, "edit_about.html")


class edit_profile (UpdateView):
    model = profile
    form_class = edit_profile_form
    template_name = "edit_profile.html"
    success_url = ("http://127.0.0.1:8000/about/")


class edit_post (UpdateView):
    model = post
    form_class = edit_post_form
    template_name = "edit_post.html"
    success_url = ("http://127.0.0.1:8000/user_profile/")


class delete_post (DeleteView):
    model = post
    template_name = "delete_post.html"
    fields = ['status']
    success_url = ("http://127.0.0.1:8000/user_profile/")


def status_form(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        status = request.POST['status']

        if request.FILES.get('photo', False):
            photo = request.FILES['photo']
            if status == '':
                messages.error(request, "You have to write.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                status_database = post(
                    username=username, name=name, status=status, photo=photo)
                status_database.save()
                messages.success(request, "Posted")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            if status == '':
                messages.error(request, "You have to write.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                status_database = post(
                    username=username, name=name, status=status)
                status_database.save()
                messages.success(request, "Posted")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comment_form(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        post_id = request.POST['post_id']
        comment = request.POST['comment']

        if comment == "":
            messages.error("You have to write something")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            comment_database = user_comment(
                username=username, name=name, post_id=post_id, comment=comment)
            comment_database.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class community (ListView):
    model = post
    template_name = "community.html"
    ordering = ['-id']

    

    def get_context_data(self, *args, **kwargs):
        context = super(community, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['profile_list'] = profile.objects.all()
        return context


class community_full (DetailView):
    model = post
    template_name = "community_full.html"

    def get_context_data(self, *args, **kwargs):
        context = super(community_full, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['comment_count'] = user_comment.objects.filter(post_id = self.kwargs['pk']).aggregate(sum_all=Sum('comment_count')).get('sum_all')
        return context


def friend_request_form(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        friend_user_name = request.POST['friend_user_name']

        if friend_request.objects.filter(username=username, friend_user_name=friend_user_name):
            messages.error(request, "Already Requested")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif friend_list.objects.filter(username=username, request_user_name = friend_user_name):
            messages.error(request, "Already Added")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            friend_request_database = friend_request(
                username=username, name=name, friend_user_name=friend_user_name)
            friend_request_database.save()
            messages.success(request, "Request Sent")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def friend_list_form(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        request_user_name = request.POST['request_user_name']
        request_name = request.POST['request_name']
        if friend_list.objects.filter(username=username, request_user_name=request_user_name):
            messages.error(request, "Already Accepted")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:

            friend_list_database = friend_list(
                    username=username, name=name, request_user_name=request_user_name, request_name=request_name)
            friend_list_database.save()
            messages.success(request, "Accepted")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class user_friend_request (ListView):
    model = friend_request
    template_name = "friend_request.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(user_friend_request, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['friend'] = friend_list.objects.all()
        context['profile_list'] = profile.objects.all()
        return context

class user_friend_list (ListView):
    model = friend_list
    template_name = "friend_list.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(user_friend_list, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['profile_list'] = profile.objects.all()
        return context

class user_chat (DetailView):
    model = profile
    template_name = "chat.html"

    def get_context_data(self, *args, **kwargs):
        context = super(user_chat, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['chat_list'] = chat.objects.all()
        return context

def chat_form (request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        chat_user_name = request.POST['chat_user_name']
        chat_name = request.POST['chat_name']
        message = request.POST['message']

        if message == "":
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            chat_database = chat(username = username, name = name, chat_user_name = chat_user_name, chat_name = chat_name, message = message)
            chat_database.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class chat_list (ListView):
    model = profile
    template_name = "chat_list.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(chat_list, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['chat_list'] = chat.objects.all()
        context['profile_list'] = profile.objects.all()
        return context



def signinn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password incorrect')

    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                login(request, user)
                send_mail(
                    'Your account created successfully.',
                    'Hey ' + first_name,
                    'createmysite.pw@gmail.com',
                    [email],
                    fail_silently=False,
                    html_message='Hey ' + first_name +
                    '<br><br>Your account created successfully.',
                )
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("/")
