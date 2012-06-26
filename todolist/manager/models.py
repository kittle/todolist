from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoItem(models.Model):
    user = models.ForeignKey(User)
    todo = models.TextField()
    priority = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        if self.priority:
            return self.todo + " (priority: %s)" % self.priority
        else:
            return self.todo
    
