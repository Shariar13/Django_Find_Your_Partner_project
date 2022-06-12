from django.contrib import admin
from .models import profile
from .models import post
from .models import user_comment
from .models import friend_request
from .models import friend_list
from .models import chat

admin.site.register (profile)
admin.site.register (post)
admin.site.register (user_comment)
admin.site.register (friend_request)
admin.site.register (friend_list)
admin.site.register (chat)
