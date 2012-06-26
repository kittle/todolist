from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group#
from django.contrib.sites.models import Site

from models import TodoItem


class TodoItemAdmin(admin.ModelAdmin):
    fields = ['todo', 'priority']
    
    def queryset(self, request):
        qs = super(TodoItemAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    
    
#admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
#admin.site.register(User, MyUserAdmin)

admin.site.register(TodoItem, admin_class=TodoItemAdmin)
#admin.site.register(TodoItem, TodoItemAdmin)
