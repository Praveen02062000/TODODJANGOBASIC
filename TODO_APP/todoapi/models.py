from django.db import models

# Create your models here.




class TODOTABLE(models.Model):
    todovalue = models.CharField(max_length=1000)
    todostatus= models.BooleanField(null=False)





"""
json = datatype = dict(python)
key - value
{
    "todovalue":"hsadashdahjsd",
    "....."
}

"""