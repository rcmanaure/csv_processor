from django.db import models

# Create your models here.
from chunked_upload.models import ChunkedUpload

# 'ChunkedUpload' class provides almost everything for you.
# if you need to tweak it little further, create a model class
# by inheriting "chunked_upload.models.AbstractChunkedUpload" class
MyChunkedUpload = ChunkedUpload


class CsvFiles(models.Model):

    filename = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    csv = models.FileField(upload_to="csv_processed/")

    def __str__(self):
        return self.filename
