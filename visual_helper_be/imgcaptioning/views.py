from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import base64
import numpy as np
import cv2


# Create your views here.
class ImageCaptioning(APIView): 
    """
        이미지 캡셔닝
        입력: base64 img str
        출력: str 캡셔닝 텍스트
    """
    @swagger_auto_schema(request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
    ))
    def post(self, request, format=None):
        """"""
        # request deserialize
        # img base64 str to numpy array
        if request.method == "POST":
            try:
                # print(request.data['img'])
                b64_img_byte_str = base64.b64decode(request.data['img'])
                tmp = np.frombuffer(b64_img_byte_str, np.uint8)
                img = cv2.imdecode(np.frombuffer(b64_img_byte_str, np.uint8), -1)
                # print(img)
                result = img.shape
            except Exception as e:
                print(e)
                result = "not valid"
        else:
            result = "request method must be POST"

        # model load

        # inference

        return Response({"shape":result}, content_type=u"application/json; charset=utf-8")