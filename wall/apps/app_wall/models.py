# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
    def register(self, postData):
        print "in def1"
        results = {'status': True, 'errors': [],'user':None}
        if not postData['first_name'] or len(postData['first_name']) <3:
            print "fname error"
            results['status'] = False
            results['errors'].append("Please enter valid first name")
        if not postData['last_name'] or len(postData['last_name']) <3:
            results['status'] = False
            results['errors'].append("Please enter valid last name")
        if not postData['emailid']:
            results['status'] = False
            results['errors'].append("Please enter valid emailid")
        if not postData['password'] or len(postData['password']) <4:
            results['status'] = False
            results['errors'].append("Password must be atleat 4 characters long")
        if postData['reenterpassword'] != postData['password']:
            results['status'] = False
            results['errors'].append("Passwords do not match")
        x = User.objects.filter(emailid = postData['emailid'])
        try:
            if x[0]:
                results['errors'].append("It already exists")
                results['status'] = False
        except:
            if results['status']:
                password = postData['password'].encode() # to get from unicode to string
                hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                print hashed
                y = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], emailid=postData['emailid'], password=hashed)
                y.save()
                results['user'] = y
        return results

    def loginval(self, postData):
        results = {'status': True, 'errors': [],'user':None}
        if not postData['emailid']:
            results['status'] = False
            results['errors'].append("Please enter valid emailid")
        print "asdfghjkl"
        if not postData['password'] or len(postData['password']) <4:
            results['status'] = False
            results['errors'].append("Password must be atleat 4 characters long")
        if results['status'] == True:
            x = User.objects.filter(emailid = postData['emailid'])
        #print x
        
            try:
                if x[0]:
                    print "in################# "
                    print x[0].password
                    password = postData['password'].encode()
                    y = x[0].password.encode()
                    if bcrypt.hashpw(password,y) == y:
                        results['status'] = True
                        print ("*****It matches**********")
                        results['user'] = x[0]
                    else:
                        results['status'] =False
                        results['errors'].append("Invalid credentials")
                        print ("*****It doesnt match**********")
            except:
                results['status'] =False
                print "please regitser"
                results['errors'].append("Please Register")
        return results
    
    def addmsgs(request,postData,sessiondata):
        print " In addmsgs %%%%%%%%%%%"
        results = {'status': True, 'errors': []}
        if len(postData['messages'])<1:
            print "In validation "
            result['status'] = False
            results['errors'].append("Please enter a valid post")
            return results
        user1 = User.objects.get(id = sessiondata['id'])
        print "Successfully done@@@@@@@@@@@@@@"
        if postData['messages']:
            Message.objects.create(message=postData['messages'],user1 = user1)
            results['status'] = True
            print "Successfully done!!!!!!!!!"
        print "Not Succesful*************"
        return results

    def addcomments(request,postData,sessiondata):
        print " In addmsgs %%%%%%%%%%%"
        results = {'status': True, 'errors': []}
        if len(postData['commenting'])<1:
            print "In validation "
            result['status'] = False
            results['errors'].append("Please enter a valid post")
            return results
        user = User.objects.get(id = sessiondata['id'])
        #print postData
        print postData['msgid']
        message = Message.objects.get(id = postData['msgid'])
      
        if postData['commenting']:
            Comment.objects.create(comment=postData['commenting'],user = user, message = message)
            results['status'] = True
            print "Successfully done!!!!!!!!!"
        print "Not Succesful*************"
        return results
        

class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    emailid = models.CharField(max_length=78)
    password = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    #users1
    #users
class Message(models.Model):
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user1 = models.ForeignKey(User, related_name="users1")
    #msg
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name="users")
    message = models.ForeignKey(Message, related_name="msg")


 
    
