from django.db import models

# Create your models here.

#User model that creates User table in database
#Has username (primary key), email  and password attributes
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length = 50, primary_key = True)
    password = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.username)
