from taggit.managers import TaggableManager # type: ignore
from django.conf import settings # type: ignore
from django.urls import reverse  # type: ignore
from django.db import models # type: ignore
from django.utils import timezone  # type: ignore
from django.db.models.functions import Now  # type: ignore

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
            
            
            )



class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish'
                            )
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    
    body=models.TextField(max_length=250)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)    
    updated=models.DateTimeField(auto_now=True)
    
    status= models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    
    )
    
    objects = models.Manager()
    published=PublishedManager()
    
    class Meta:
        ordering =['-publish']
        indexes=[
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("myapp:post_detail",
                       args=[
                           self.publish.year,
                           self.publish.month,
                           self.publish.day,                           
                           self.slug
                           
                           
                           ])
        
        
    tags=TaggableManager()
        
    
    
#This is the comments model
class Comment(models.Model):
    post = models.ForeignKey(
    Post, 
    on_delete=models.CASCADE,
    related_name='comments',
    )
    
    name=models.CharField(max_length=80)
    email= models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering=['created']
        indexes=[
            models.Index(fields=['created']),
        ]
        
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    
    
    