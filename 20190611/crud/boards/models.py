from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

def board_image_path(instance, filename):
    return f'boards/{instance.pk}번글/images/{filename}'

class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to=board_image_path(),
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality':90},
    )
    created_at = models.DateTimeField(auto_now_add=True) # 글을 생성한 최초의 시간
    updated_at = models.DateTimeField(auto_now=True) # 글을 수정한 최근 시간

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'

