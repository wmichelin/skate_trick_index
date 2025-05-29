from django.db import models
from django.contrib.auth.models import User

class TrickCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Trick Categories"

class SkateTrick(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('pro', 'Pro'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(TrickCategory, on_delete=models.CASCADE, related_name='tricks')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    image = models.ImageField(upload_to='trick_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class UserProgress(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('learning', 'Learning'),
        ('landed', 'Landed'),
        ('mastered', 'Mastered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trick = models.ForeignKey(SkateTrick, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    notes = models.TextField(blank=True)
    last_practiced = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'trick')
        verbose_name_plural = "User Progress"
    
    def __str__(self):
        return f"{self.user.username} - {self.trick.name} ({self.status})" 