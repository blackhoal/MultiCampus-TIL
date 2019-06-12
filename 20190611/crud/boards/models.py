from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 글을 생성한 최초의 시간
    updated_at = models.DateTimeField(auto_now=True) # 글을 수정한 최근 시간

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'

