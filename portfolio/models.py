from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    technologies = models.CharField(max_length=200, help_text="e.g., Python, Django, React")
    live_link = models.URLField(blank=True, null=True, help_text="Optional link to live site")
    
    # Bento layout size option
    SIZE_CHOICES = [
        ('normal', 'Standard Box'),
        ('wide', 'Wide Box (Spans 2 columns)'),
    ]
    card_size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='normal')

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=100, default="Your Name")
    tagline = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return "About Me Data"

class Skill(models.Model):
    name = models.CharField(max_length=50, help_text="e.g. Python")
    
    def __str__(self):
        return self.name
# (Keep your existing Project, About, and Skill models above this...)

class Education(models.Model):
    degree = models.CharField(max_length=200, help_text="e.g., B.Tech in Computer Science & Engineering")
    institution = models.CharField(max_length=200, help_text="e.g., University Name")
    year = models.CharField(max_length=50, help_text="e.g., 2023 - 2027")
    description = models.TextField(blank=True, null=True, help_text="Optional short details")

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Certification(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., AWS Certified Cloud Practitioner")
    issuer = models.CharField(max_length=200, help_text="e.g., Amazon Web Services")
    date_earned = models.CharField(max_length=50, help_text="e.g., June 2025")
    credential_link = models.URLField(blank=True, null=True, help_text="Link to certificate")

    def __str__(self):
        return f"{self.title} ({self.issuer})"

class ProfileLink(models.Model):
    CATEGORY_CHOICES = [
        ('social', 'Social Media'),
        ('coding', 'Coding & Practice Platform'),
    ]
    name = models.CharField(max_length=100, help_text="e.g., LeetCode, GitHub, Codeforces")
    url = models.URLField(help_text="Link to your profile")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='coding')
    
    # NEW: Username field to fetch live data
    username = models.CharField(max_length=100, blank=True, null=True, help_text="Exact username on the platform (Required for live stats)")

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Research(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the research paper or project")
    publication = models.CharField(max_length=200, help_text="e.g., IEEE, ArXiv, University Journal")
    date = models.CharField(max_length=50, help_text="e.g., October 2026")
    description = models.TextField(help_text="Brief abstract or summary of your contribution")
    link = models.URLField(blank=True, null=True, help_text="Link to the published paper or PDF")

    def __str__(self):
        return self.title