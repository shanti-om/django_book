from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
                                                 self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])
