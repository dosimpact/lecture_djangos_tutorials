from django.contrib import admin
from .models import ImageUploadModel,Profile,FileUploadModel
# Register your models here.

admin.site.register(FileUploadModel)
admin.site.register(ImageUploadModel)
admin.site.register(Profile)
