from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):

    # item data
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)

    # meta data
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Project {self.id}: {self.title}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):

    # item data
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    start_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )

    # meta data
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # relational
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta():
        ordering = ['done']


    def __str__(self):
        status = "Done" if self.done else "Not Done"
        return f'Task {self.id}: {self.title} ({status}) [Project ID: {self.project_id}]'

