from django.db import models


class PageVisit(models.Model):
    # db -> table 
    # id -> primary key > authfield -> 1, 2, 3...
    path = models.TextField() # col
    timestamp = models.DateTimeField(auto_now_add=True) # col
