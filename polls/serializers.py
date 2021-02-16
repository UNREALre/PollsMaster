# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Poll, Question, Answer, UserAnswer, UserAnswerChoice


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'option_text', )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'text', 'q_type', 'answers', )


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'start_date', 'end_date', 'description', 'questions', )


class PollUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'end_date', 'description', )


class UserAnswerChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswerChoice
        fields = ('id', 'user_answer', 'choice', )


class UserAnswerTextSerializer(serializers.ModelSerializer):
    user_choices = UserAnswerChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = UserAnswer
        fields = ('id', 'user_id', 'question', 'text_answer', 'user_choices', )


class QuestionResultSerializer(serializers.ModelSerializer):
    user_answers = UserAnswerTextSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'text', 'q_type', 'user_answers', )


class PollResultSerializer(serializers.ModelSerializer):
    questions = QuestionResultSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'start_date', 'end_date', 'description', 'questions', )

