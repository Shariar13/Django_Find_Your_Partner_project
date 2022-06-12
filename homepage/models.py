from email.policy import default
from django.db import models
from django.db.models.fields.files import ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings 



class profile(models.Model):
    name = models.CharField (max_length=99,null=True,blank=True)
    username = models.CharField (max_length=99,null=True,blank=True)
    height = models.CharField (max_length=99)
    weight = models.CharField (max_length=99)
    eyes = models.CharField (max_length=99)
    hair = models.CharField (max_length=99)
    education = models.CharField (max_length=99)
    phone = models.CharField (max_length=99)
    email = models.CharField (max_length=99)
    description = models.TextField ()
    gender = models.CharField (max_length=99,null=True)
    cover_pic = models.ImageField(upload_to='photo/', blank=True, null=True, default = "photo/cover.png")
    profile_pic = models.ImageField(upload_to='photo/', blank=True, null=True, default = "photo/user.jpg")

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

    @property
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/1.jpg"

    @property
    def get_photo_url(self):
        if self.cover_pic and hasattr(self.cover_pic, 'url'):
            return self.cover_pic.url
        else:
            return "/static/1.jpg"

class post (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    status = models.TextField ()
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    date = models.DateTimeField (auto_now_add=True,null = True)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return None

class user_comment (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    post_id = models.IntegerField ()
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField (auto_now_add=True,null = True)
    comment_count = models.IntegerField (null = True, default=1)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class friend_request (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    friend_user_name = models.CharField (max_length=99)
    date = models.DateTimeField (auto_now_add=True,null = True)
    request_count = models.IntegerField (null = True, default=1)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class friend_list (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    request_user_name = models.CharField (max_length=99)
    request_name = models.CharField (max_length=99)
    date = models.DateTimeField (auto_now_add=True,null = True)
    friend_count = models.IntegerField (null = True, default=1)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class chat (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    chat_user_name = models.CharField (max_length=99)
    chat_name = models.CharField (max_length=99)
    message = models.TextField (null=True)
    date = models.DateTimeField (auto_now_add=True)
    only_date = models.DateField (auto_now_add=True)
    friend_count = models.IntegerField (null = True, default=1)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

   

