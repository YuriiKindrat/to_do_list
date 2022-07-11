from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True, default="")
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tags", related_name="tasks")

    class Meta:
        ordering = ["status", "-datetime"]

    def __str__(self):
        return self.content


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
