from django.db import models


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
    description = models.TextField(verbose_name="About Project")
    image = models.ImageField(default="None")

    def __str__(self):
        return self.project_name


class Client(models.Model):
    image = models.ImageField(default="None")
    name = models.CharField(max_length=100, verbose_name="Client name")
    comment = models.TextField(verbose_name="Client says")

    def __str__(self):
        return self.name
