from django.db import models

class Base(models.Model):
    ACTIVE = 1
    INACTIVE =0
    DELETE = -1
    STATUS_CHOISE =[(ACTIVE,'Active'),(INACTIVE,'Inactive'),(DELETE,'Delete') ]   
    id = models.AutoField(primary_key=True,db_index=True)
    status = models.IntegerField(default=1, choices=STATUS_CHOISE,db_index=True)

    class Meta:
        abstract = True

