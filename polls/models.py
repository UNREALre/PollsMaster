# -*- coding: utf-8 -*-

from django.db import models


class Poll(models.Model):
    """Модель опроса."""

    name = models.CharField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        ordering = ('start_date', )


class Question(models.Model):
    """Модуль вопроса опроса."""

    QUESTION_TYPE = (
        ('TXT', 'Ответ с текстом'),
        ('SC', 'Ответ с выбором варианта'),
        ('MC', 'Ответ с выбором нескольких вариантов')

    )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    q_type = models.CharField(max_length=3, choices=QUESTION_TYPE)


class Answer(models.Model):
    """Модель ответа на вопрос (когда тип вопроса ответ с вариантом)."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    option_text = models.TextField()


class UserAnswer(models.Model):
    """Модель ответов пользователей на вопросы."""

    user_id = models.IntegerField()  # int - потому что опросы проходят анонимно
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    text_answer = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('user_id', 'question')


class UserAnswerChoice(models.Model):
    """Модель выбранных ответов пользователя."""

    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE, related_name='user_choices')
    choice = models.ForeignKey(Answer, on_delete=models.CASCADE)
