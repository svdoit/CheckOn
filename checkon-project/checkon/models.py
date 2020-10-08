from django.db import models

# Create your models here.

class Item(models.Model):
    itemName = models.CharField(max_length=200)
    itemImg = models.ImageField(upload_to='images/', blank=True)
    itemPrice = models.CharField(max_length=20)
    category = models.IntegerField(max_length=10)

# 0. 과일, 견과
# 1. 수산
# 2. 정육, 계란
# 3.채소
# 4.쌀잡곡
# 5.유제품
# 6.반찬, 간편식
# 7.액체류(생수, 음료, 주류)
# 8.과자, 빵
# 9.즉석조리(라면, 통조림, 소스장류)
# 10.건강식품
