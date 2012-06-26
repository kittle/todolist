import re

from django.contrib.auth.models import User

from piston.handler import BaseHandler
from piston.utils import rc, throttle, require_mime, require_extended

from models import TodoItem


class TodoItemHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    fields = ('id', 'todo', 'priority')
    #exclude = ('id', re.compile(r'^private_'))
    model = TodoItem

    @require_extended
    def create(self, request, *args, **kw):
        data = request.data
        todoitem = self.model(user=request.user, todo=data['todo'],
                priority=data['priority'])
        todoitem.save()
        #resp = rc.CREATED
        return todoitem

    def read(self, request, todoitem_id=None):
        if todoitem_id:
            todoitem = TodoItem.objects.get(id=todoitem_id, user=request.user)
        else:
            todoitem = TodoItem.objects.filter(user=request.user)
        return todoitem

    @require_extended
    def update(self, request, todoitem_id):
        data = request.data
        todoitem = TodoItem.objects.get(id=todoitem_id, user=request.user)
        todoitem.todo = data['todo']
        todoitem.priority = data['priority']
        todoitem.save()
        return todoitem

    def delete(self, request, todoitem_id):
        todoitem = TodoItem.objects.get(id=todoitem_id, user=request.user)
        #if not request.user == post.author:
        #    return rc.FORBIDDEN # returns HTTP 401
        todoitem.delete()
        return rc.DELETED # returns HTTP 204

