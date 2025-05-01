from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # on_delete=models.CASCADE : User 계정정보가 삭제되면 해당 Profile도 같이 삭제
    # related_name='profile' : User Db와 join 개념이라고 생각하면됨. 검색 및 호출시 사용

    image = models.ImageField(upload_to='profile/', null=True)
    # upload_to='profile/' : /midia/profile/ 폴더에 저장
    nickname = models.CharField(max_length=20, unique=True, null=True)
    # unique=True : uid처럼 DB Table에서 하나만 있는것.
    message = models.CharField(max_length=100, null=True)
