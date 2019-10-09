from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.conf import settings

from .models import ImageUploadModel
from .forms import UploadImageForm
#from .opencv_dface import opencv_dface




def index(request):
    return HttpResponse("opencv")

def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print('############',uploaded_file_url)
            return render(request, 'opencvwebapp/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})

    else:
        form = UploadImageForm()
        return render(request, 'opencvwebapp/uimage.html', {'form': form})

def dface(request):
    return HttpResponse("dface")