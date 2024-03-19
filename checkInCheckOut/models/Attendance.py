# models.py

from django.db import models
from userLogin.models.CustomeUserModel import CustomeUserModel

class Attendance(models.Model):
    user = models.ForeignKey(CustomeUserModel, on_delete=models.CASCADE,verbose_name='User')
    check_in_time = models.DateTimeField(null=True, blank=True,verbose_name='Check in')
    check_out_time = models.DateTimeField(null=True, blank=True,verbose_name='Check out')
