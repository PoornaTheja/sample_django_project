from django.shortcuts import render
from rest_framework import viewsets

from .serializers import User_Serializer
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all().order_by('name')
    serializer_class = User_Serializer
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all().order_by('name')
    serializer_class = User_Serializer
    
    
def product_home_view(request):
    product_list = product.objects.all()
    context = {"list" : product_list}
    
    return render(request, 'product/home.html', context)

def product_sep_view(request, prod_name):
    cur_product = product.objects.get(name = prod_name)
    context = {"product" : cur_product}
    
    return render(request, 'product/sep.html', context)


# from django.http import HttpResponse
# from django.shortcuts import render
from django.urls import reverse
# from .models import *
# from django.core.mail import EmailMessage
# from django.views.decorators import gzip
# from django.http import StreamingHttpResponse
import cv2
import numpy as np
from django.core.files.base import ContentFile
# import threading

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
    
#     def get_gray_frame(self):
#         image = self.frame
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
# def gray_gen(camera):
#     while True:
#         frame = camera.get_gray_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# cam = VideoCamera()

# @gzip.gzip_page
# def video_stream(request):
#     try:
#         # cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass
#     print("######")
#     return render(request, 'basic.html')


# @gzip.gzip_page
# def gray_video_stream(request):
#     try:
#         # cam = VideoCamera()
#         return StreamingHttpResponse(gray_gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass
#     print("!!!!!!")
#     return render(request, 'basic.html')


def home(request):
    # color_url = reverse('video_stream')
    # gray_url = reverse('gray_video_stream')
    # context = {"color" : color_url,
    #            "gray" : gray_url}    
    
    # return render(request, 'home.html', context)
    return render(request, 'basic.html')


def rgb_gray(request):
    context = {}
    if request.method == "POST":
        request.FILES['img'].name = request.POST["title"] + "_color.jpg"
        print(request.POST)
        print(request.FILES)
        form = image_form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            img = form.cleaned_data.get("img")
            obj = image.objects.create(title = title, img = img)            

            np_img = cv2.imread("media/" + str(obj.img))
            gray_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
            
            gray_img1 = cv2.imencode('.jpg', gray_img)[1]
            file = ContentFile(gray_img1)
            obj.gray.save(title + "_gray.jpg", file, save=True)
            obj.save()
            
            context['form']= form
            context['color'] = np_img
            context['gray'] = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
            context['current_img'] = obj
            
    else:
        form = image_form()
        context['form']= form
        
    return render(request, "rgb_gray/home.html", context)
    