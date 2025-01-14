from django.db import models
from django.contrib.postgres.fields import ArrayField


class ETC(models.Model):  # 관련 페이지
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Event(models.Model):
    id = models.CharField(max_length=50, primary_key=True, null=False)
    title = models.CharField(max_length=50)  # 대회제목
    create_date = models.DateTimeField()  # 작성날짜

    # 개최기간
    start_date = models.DateField()
    end_date = models.DateField()

    # 개최장소 이름, 구글맵 링크
    location = models.CharField(max_length=50)
    map = models.CharField(max_length=255)

    # 관련 내용, etc 모델의 id를 참조
    others = models.ManyToManyField(ETC, blank=True)

    # 포스터 사진
    image_top = models.ImageField(upload_to="posters/top/", blank=True)
    image_bottom = models.ImageField(upload_to="posters/bottom/", blank=True)

    # 개최리그
    leagues = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    def __str__(self):
        return self.title
