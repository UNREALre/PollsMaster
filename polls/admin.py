# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Answer, Poll, Question, UserAnswer, UserAnswerChoice


class AnswerAdmin(admin.ModelAdmin):
    pass


class PollAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class UserAnswwerAdmin(admin.ModelAdmin):
    pass


class UserAnswerChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer, UserAnswwerAdmin)
admin.site.register(UserAnswerChoice, UserAnswerChoiceAdmin)
