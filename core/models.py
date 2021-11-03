from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    """
    Base model for all the classes
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class UserProfile(BaseModel):
    contact_number = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    profession = models.CharField(max_length=200)
    earning = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)


class BusinessEntity(BaseModel):
    name = models.CharField(max_length=200)
    city_headquatered = models.CharField(max_length=200) #city of origin
    type_of_business = models.CharField(max_length=200) #what type of business is it


class Expense(BaseModel):
    business_entity = models.ForeignKey(BusinessEntity,on_delete=models.SET_NULL,null=True,blank=True)
    expense_amount = models.FloatField()
    description = models.TextField(blank=True,null=True)






