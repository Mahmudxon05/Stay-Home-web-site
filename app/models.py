from django.db import models
# Create your models here.


#--------------------_HOME_Class--------------------#

class Home(models.Model):
    phone = models.CharField(max_length=13)
    photo = models.ImageField(upload_to='home/')
    email = models.EmailField()
    title = models.CharField(max_length=110)
    text = models.TextField()

#--------------------_Services_Class_-------------------#

class OurServices(models.Model):
    text = models.TextField()


class ServicesTypes(models.Model):
    title = models.CharField(max_length=110)
    text = models.TextField()
    def __str__(self):
        return self.title
   
#--------------------_Listening_Classs_--------------------#


class Property(models.Model):
    title = models.CharField(max_length=110)
    

class OurProperty(models.Model):
    name = models.CharField(max_length=110)
    image = models.ImageField(upload_to='ourproperty/')
    country = models.CharField(max_length=100)
    price = models.IntegerField()
    rent = models.CharField(max_length=100)
    sale = models.CharField(max_length=100)
    bath = models.CharField(max_length=100)
    bds = models.CharField(max_length=110)

    def __str__(self):
        return self.name
    

#---------------------_About_Class_--------------------#

class About(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='about/')


class Agency(models.Model):
    title = models.CharField(max_length=100)
    text_one =models.TextField()
    text_two = models.TextField()
    text_three = models.TextField() 
    image = models.ImageField(upload_to='about1/')

#--------------------_How-it-Works_Classes_--------------------#

class How_it_Works(models.Model):
    title = models.CharField(max_length=110)
    text = models.TextField()


class Dating(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
    

class Offer(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='offfer/')
    price = models.IntegerField()
    text = models.TextField()    

#----------------------_Agent_Classes_-------------------# 

class OurAgent(models.Model):
    title = models.CharField(max_length=110)  

class Agent(models.Model):
    title = models.CharField(max_length=110)
    full_name = models.CharField(max_length=110)
    job = models.CharField(max_length=110)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='agenccy/')

    def __str__(self):
        return self.full_name 
    

#--------------------_Blog_--------------------#

class OurBlog(models.Model):
    title = models.CharField(max_length=110)
    text = models.TextField()


class Blog(models.Model):
    day =models.IntegerField()
    year = models.IntegerField()
    month = models.CharField(max_length=110)
    image = models.ImageField(upload_to='blog/')
    text = models.TextField()
    question = models.CharField(max_length=110)

    

#--------------------_Contact_Class--------------------#

class Read(models.Model):
    sharh = models.TextField()
    title = models.CharField(max_length=110)


class Contact(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    image = models.ImageField(upload_to='contact/')
    job = models.CharField(max_length=110)


class Info(models.Model):
    cont = models.CharField(max_length=110)
    title = models.CharField(max_length=110)
    text = models.TextField()


class Input(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    subject = models.CharField(max_length=110)
    message = models.TextField()    


class Information(models.Model):
    address = models.CharField(max_length=110)
    email = models.EmailField()
    phone =models.CharField(max_length=13)
    web = models.URLField()


class Stayhome(models.Model):
    title = models.CharField(max_length=110)
    text = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()


class Question(models.Model):
    title = models.CharField(max_length=110)
    address = models.CharField(max_length=110)
    phone = models.CharField(max_length=13)
    domain = models.URLField()


        
    





