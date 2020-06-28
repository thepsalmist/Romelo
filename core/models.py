from django.db import models
from django.urls import reverse


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return "About Us"


class Service(models.Model):
    title = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100, verbose_name="Project name")
    slug = models.SlugField(null=True)
    description = models.TextField(
        help_text="Client Name, Project Category, Project date, Project Description",
    )
    main_photo = models.ImageField(default="None")
    photo_2 = models.ImageField(blank=True, null=True)
    photo_3 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse("core:project", args=[self.slug])


class Client(models.Model):
    image = models.ImageField(default="None")
    name = models.CharField(max_length=100, verbose_name="Client name")
    client_title = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(verbose_name="Client says")

    def __str__(self):
        return self.name


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="Team", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}| {self.position}"


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=240)

    def __str__(self):
        return self.name
