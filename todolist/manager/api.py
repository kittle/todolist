import re

from django.contrib.auth.models import User

from piston.handler import BaseHandler
from piston.utils import rc, throttle, require_mime, require_extended

from models import TodoItem


def raise_404(method):
    def wrap(*args, **kwargs):
        from django.core.exceptions import ObjectDoesNotExist
        from django.http import Http404
        try:
            return method(*args, **kwargs)
        except ObjectDoesNotExist, ex:
            raise Http404(ex.message)
    return wrap


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

    @raise_404
    def read(self, request, todoitem_id=None):
        if todoitem_id:
            todoitem = TodoItem.objects.get(id=todoitem_id, user=request.user)
        else:
            todoitem = TodoItem.objects.filter(user=request.user)
        return todoitem

    @raise_404
    @require_extended
    def update(self, request, todoitem_id):
        data = request.data
        todoitem = TodoItem.objects.get(id=todoitem_id, user=request.user)
        todoitem.todo = data['todo']
        todoitem.priority = data['priority']
        todoitem.save()
        return todoitem

    @raise_404
    def delete(self, request, todoitem_id):
        todoitem = TodoItem.objects.get(id=todoitem_id, user=request.user)
        #if not request.user == post.author:
        #    return rc.FORBIDDEN # returns HTTP 401
        todoitem.delete()
        return rc.DELETED # returns HTTP 204

