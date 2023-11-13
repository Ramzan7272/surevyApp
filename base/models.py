from django.db import models


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.question_text[:10]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    value = models.CharField(max_length=1, default='A')

    def __str__(self) -> str:
        return self.choice_text[:10]


class Answer(models.Model):
    m_or_f = models.CharField(max_length=10, null=True)
    answers = models.JSONField(default=dict)
