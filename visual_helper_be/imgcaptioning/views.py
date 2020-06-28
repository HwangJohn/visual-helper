from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import base64
import numpy as np
import cv2
import os
import six
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="credential.json"

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
                result = "not valid image"
        else:
            result = "request method must be POST"
            return Response({"result":result}, content_type=u"application/json; charset=utf-8")


        # inference
        caption = evaluate(img)

        # translation
        ## 환경변수에 GOOGLE_APPLICATION_CREDENTIALS 옵션이 셋팅되어있어야 함
        ## https://cloud.google.com/translate/docs/basic/setup-basic
        result = google_translation(caption)

        return Response({"result":result}, content_type=u"application/json; charset=utf-8")

def google_translation(text:str) -> str:
    """ translating en to ko
        입력: 영문 캡셔닝 결과
        출력: 한글 번역 결과 
    """
    try:
        # target lan을 한국어로 고정
        target = "ko"

        translate_client = translate.Client()

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = translate_client.translate(
            text, target_language=target)

        print(u'Text: {}'.format(result['input']))
        print(u'Translation: {}'.format(result['translatedText']))
        print(u'Detected source language: {}'.format(
            result['detectedSourceLanguage']))
    except Exception as e:
        print(e)
        return "Error, not translated"

    return result['translatedText']

def evaluate(img:np.array)->str:
    """ Image Captioning
        입력: np.array uint8 이미지 데이터
        출력: str caption 데이터
    """