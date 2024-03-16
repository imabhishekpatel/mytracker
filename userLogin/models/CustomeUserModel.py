from django.contrib.auth.models import AbstractUser
from django.db import models
from coreApp.models.baseModel import Base


class CustomeUserModel(AbstractUser,Base):
    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'              
        db_table = "user" 