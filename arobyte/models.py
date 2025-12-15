from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Volunteer(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=30)
    message=models.TextField()
    college_name=models.CharField(max_length=100, default='', verbose_name='College/Company Name')
    preprofessional=models.CharField(max_length=100, default='', verbose_name='Preprofessional')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = CKEditor5Field('Content', config_name='extends')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='extends')
    priority = models.CharField(max_length=20, choices=[
        ('high', 'High Priority'),
        ('medium', 'Medium Priority'),
        ('low', 'Low Priority')
    ], default='medium')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True, help_text="Optional. When this announcement should stop showing.")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
