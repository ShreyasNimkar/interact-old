from audioop import reverse
import imp
from django.db import models
from user.models import User
from django.utils import timezone
# Create your models here.

from group.models import Group


class GrpPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(default=timezone.now(),blank=True)
    message=models.TextField()
    group=models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return (self.message+' by '+self.user.username)

    class Meta:
        ordering=['-created_at']
