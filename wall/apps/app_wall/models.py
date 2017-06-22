# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    emailid = models.CharField(max_length=78)
    password = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #users1
class Message(models.Model):
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user1 = models.ForeignKey(User, related_name="users1")
    #users
    #msg
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name="users")
    message = models.ForeignKey(Message, related_name="msg")



    
