# Create your models here.
from django.db import models
import uuid

class Memes(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        pictureName = models.CharField(max_length=50)
        url = models.CharField(max_length=300)
        description = models.CharField(max_length=500)
        viewCount = models.IntegerField(default = 0)
        Tags = models.ManyToManyField('Tags')

        def tag_list(self):
                return [str(tag) for tag in self.Tags.all()]

        def __str__(self):
                return self.pictureName


class Tags(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
                return self.name