from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'Categories'
  
  
  
  
class Product(models.Model):
    name             = models.CharField(max_length=200)
    description      = models.TextField()
    price            = models.DecimalField(max_digits=10, decimal_places=2)
    stock            = models.IntegerField(default=0)
    image            = models.ImageField(
                       upload_to='products/',
                       blank=True,
                       null=True
                     )
    category         = models.ForeignKey(
                      Category,
                      on_delete=models.SET_NULL,
                      null=True,
                      blank=True
                     )
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    
      
    def __str__(self):
        return self.name
    

class Profile(models.Model):
  user       = models.OneToOneField(
               User,
               on_delete=models.CASCADE
    
               )
  phone      = models.CharField(max_length=15, blank=True)
  address    = models.TextField(blank=True)
  avatar     = models.ImageField(
                upload_to='avatars/',
                blank=True,
                null=True
              )
  def __str__(self):
        return f'{self.user.username} Profile'
      

class Order(models.Model):
  
    user       = models.ForeignKey(
                   User,
                   on_delete=models.CASCADE
                 )
    products   = models.ManyToManyField(
                   Product,
                   blank=True
                 )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'