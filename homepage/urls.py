from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include





urlpatterns = [
    path('',views.home,name="home"),
    path('woman',views.woman.as_view(),name="woman"),
    path('man',views.man.as_view(),name="man"),
    path('signin/',views.signinn,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('user_profile/',views.user_profile.as_view(),name="user_profile"),
    path('about/',views.about.as_view(),name="about"),
    path('about_form/',views.about_form,name="about_form"),
    path('edit_about/',views.edit_about,name="edit_about"),
    path('edit_profile/<int:pk>',views.edit_profile.as_view(),name="edit_profile"),
    path('status_form/',views.status_form,name="status_form"),
    path('community/',views.community.as_view(),name="community"),
    path('community_full/<int:pk>',views.community_full.as_view(),name="community_full"),
    path('comment_form',views.comment_form,name="comment_form"),
    path('edit_post/<int:pk>',views.edit_post.as_view(),name="edit_post"),
    path('<int:pk>/delete_post',views.delete_post.as_view(),name="delete_post"),
    path('user_profile_view/<int:pk>',views.user_profile_view.as_view(),name="user_profile_view"),
    path('user_about/<int:pk>',views.user_about.as_view(),name="user_about"),
    path('friend_request_form',views.friend_request_form,name="friend_request_form"),
    path('user_friend_request',views.user_friend_request.as_view(),name="user_friend_request"),
    path('friend_list_form',views.friend_list_form,name="friend_list_form"),
    path('user_friend_list',views.user_friend_list.as_view(),name="user_friend_list"),
    path('user_chat/<int:pk>',views.user_chat.as_view(),name="user_chat"),
    path('chat_form',views.chat_form,name="chat_form"),
    path('chat_list',views.chat_list.as_view(),name="chat_list"),

    
    
]