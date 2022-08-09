from django.db import models

# Create your models here.

from user.models import User,Post

class Follower(models.Model):
    to_user=models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    from_user=models.ForeignKey(User,related_name='from_user',on_delete=models.CASCADE)

    def __str__(self):
        return "From {} to {}".format(self.from_user.username,self.to_user.username)

    class Meta:
        unique_together=[['to_user','from_user']]

