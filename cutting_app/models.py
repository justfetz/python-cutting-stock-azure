from django.db import models

# Create your models here.
def upload_path(instance, filename):
    return '/'.join(['images', str(instance.name), filename])