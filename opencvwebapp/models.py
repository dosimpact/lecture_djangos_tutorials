from django.db import models

# Create your models here.


#
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='images/%Y/%m/%d') #마법 > media/images/2019/10/09 에 저장되겠지..
    uploaded_at = models.DateTimeField(auto_now_add=True)

class FileUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='images/%Y/%m/%d') #마법 > media/images/2019/10/09 에 저장되겠지..
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.document.name)

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


@receiver(pre_delete, sender=ImageUploadModel)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.document.delete(False)

class Profile(models.Model):
    name = models.CharField(max_length = 10)
    image  = models.ImageField(blank = True, null = True)
    def __str__(self):
        return self.name