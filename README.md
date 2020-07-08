# visual-helper
This project is a part of the [my-little-ml-ops](https://www.facebook.com/groups/706222566865589).


## Project Objective
이 프로젝트의 목적은 딥러닝 컴퓨터 비전 기술과 자연어 처리 기술을 이용해서 시각장애인의 일상생활을 돕는 것입니다.

### Methods Used
* Django
* Image Captioning
* Google Cloud translation API

### Technologies
* tf.keras 2.1

## Project Description
데이터 소스: COCO dataset

### step 1: Base64형식의 이미지 String을 Rest api를 통해 입력으로 받음
<a href="https://drive.google.com/uc?export=view&id=1aPXfOh9sQVrdRmu8ejy3XsLfPT0dFUIB"><img src="https://drive.google.com/uc?export=view&id=1aPXfOh9sQVrdRmu8ejy3XsLfPT0dFUIB" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>
```shell
curl -X POST "http://localhost:8000/imgcaptioning/predict" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: kpIdgr6SJIQSbnO6AkrGioMs15svGivnGh6FsmC4Tfym6k8detGf4Y60UKqx80G7" -d "{  \"img\": \"b'/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/
...
ABRRRQAUUUUAf//Z'\"}"
```


### step2: request data['img'] 의 text데이터를 ImageCaptioning model로 inference
```python
# inference
caption = evaluate(img)
```

### step3: Google Cloud Translation API통해 inference결과를 한글로 번역
```python
target = "ko"
text = "There is a bowl on a table."
...
result = translate_client.translate(
	text, target_language=target)
...
```


## Getting Started
1. Install packages
```shell
dj-database-url==0.5.0
Django==3.0.2
django-cors-headers==3.2.1
django-filter==2.2.0
django-rest-framework==0.1.0
django-rest-swagger==2.2.0
djangorestframework==3.11.0
djangorestframework-camel-case==1.1.2
djangorestframework-recursive==0.1.2
drf-yasg==1.17.1
flex==6.14.1
efficientnet
scikit-learn
google-cloud-translate==2.0.1
tensorflow==2.1.0
```
2. Run Django server
```shell
$ python visual_helper_be/manage.py runserver
```

3. API Documentation
http://localhost:8000/swagger/v1

