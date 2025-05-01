from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    # ForeignKey :
    # on_delete=models.SET_NULL : 회원이 탈퇴하면 "알수없는 게시자"로 글을 유지 하게함.
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

