from django.db import models
from user.models import User
import datetime
# Create your models here.
class TestModel(models.Model):
    text=models.CharField(max_length=25)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    date_created=models.DateTimeField(default=datetime.datetime.now())