from django.db import models
from quiz.models import Quiz
from django.contrib.auth.models import User


class Results(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Results"