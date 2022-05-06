from django.db import models


class PreviousProjects(models.Model):
    projectName = models.CharField(max_length=100)
    projectDeliveryDate = models.DateTimeField()
    liveDemoDink = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.projectName


class Testimonial(models.Model):
    customerName = models.CharField(max_length=100)
    customerImage = models.ImageField()
    country = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    quot = models.TextField()
    reviewRanks = models.IntegerField(default=5)

    def __str__(self):
        return self.customerName


class MyServices(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    datetimeOfMessage = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


"""

model 
previous Projects  : in this model you will show your previous work to your potential customers  so you need to make the user experience as better as you can. 

I will give you some hints , but you have to build your own model 

Project name 
Project delivery date 
live demo link 
description 
image 
2) testimonial 
Customer name 
customer image 
country 
title 
 quot 
review ranks 

3) your services 
image 
title 
description 

4) contact me 
name 
email 
message 
datetime of message 

"""