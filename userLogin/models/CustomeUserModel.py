from django.contrib.auth.models import AbstractUser

class CustomeUserModel(AbstractUser):
    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'              
        db_table = "user" 
