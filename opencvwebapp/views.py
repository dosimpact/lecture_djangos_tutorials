from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.conf import settings

from .models import ImageUploadModel,FileUploadModel
from .forms import UploadImageForm,ImageUploadForm,ProfileUploadForm,FileUploadForm
from .opencv_dface import opencv_dface
from .opencv_sface import opencv_sface

import cv2
import numpy as np

def index(request):
    if request.method == 'POST':
        profileform = ProfileUploadForm(request.POST,request.FILES)
        if profileform.is_valid():
            profileform.save()
            return HttpResponse('OK!')
    else:
        profileform = ProfileUploadForm()
    return render(request,'opencvwebapp/index.html',{'profileform':profileform} )

def capture_video_from_cam():
    fs = FileSystemStorage()
    uploaded_file_url = fs.url('Car.mp4')
    print("##########",uploaded_file_url)
    cap = cv2.VideoCapture(uploaded_file_url)
    currentFrame = 0
    while True:

        ret, frame = cap.read()

        # Handles the mirroring of the current frame
        frame = cv2.flip(frame,1)
        currentFrame += 1

def show_video_on_page(request):
    resp = StreamingHttpResponse(capture_video_from_cam())
    return render(request, 'opencvwebapp/sface.html', {'video': resp})

def strem_file(request, *args, **kwargs):
    r = requests.get("http://host.com/file.txt", stream=True)

    resp = StreamingHttpResponse(streaming_content=r.raw)

    # In case you want to force file download in a browser 
    # resp['Content-Disposition'] = 'attachment; filename="saving-file-name.txt"'

    return resp

def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print('############',filename," -> ",uploaded_file_url)
            return render(request, 'opencvwebapp/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})

    else:
        form = UploadImageForm()
        return render(request, 'opencvwebapp/uimage.html', {'form': form})

def dface(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            # db delete
            if ImageUploadModel.objects.all().count() > 100:
                obs = ImageUploadModel.objects.all().first()
                if obs:
                    obs.delete()
            imageURL = settings.MEDIA_URL + form.instance.document.name #name-> 경로+파일명이 나오네..
            print("####### imageURL -> ",imageURL,' form.instance.document.name ',form.instance.document.name)
            opencv_dface(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'opencvwebapp/dface.html', {'form': form, 'post': post})
    else:
        form = ImageUploadForm()
    return render(request, 'opencvwebapp/dface.html', {'form': form})

def sface(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            fileURL = settings.MEDIA_URL + form.instance.document.name #name-> 경로+파일명이 나오네..
            print("####### imageURL -> ",fileURL,' form.instance.document.name ',form.instance.document.name)
            opencv_sface(settings.MEDIA_ROOT_URL + fileURL)

            return render(request, 'opencvwebapp/sface.html', {'form': form, 'post': post})
    else:
        form = ImageUploadForm()
    return render(request, 'opencvwebapp/sface.html', {'form': form})
