from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Design', 'Graphic Design'),
        ('Software', 'Software Engineering'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency_percentage = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Design', 'Graphic Design'),
        ('Software', 'Software Engineering'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    project_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
