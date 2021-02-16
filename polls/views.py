# -*- coding: utf-8 -*-

from datetime import datetime
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Poll, Question, Answer, UserAnswer
from .serializers import (PollSerializer, PollUpdateSerializer, QuestionSerializer, AnswerSerializer,
                          UserAnswerTextSerializer, UserAnswerChoiceSerializer, PollResultSerializer)


class PollAndQuestPermission(permissions.BasePermission):
    """Определяет доступ для разных действий с моделью Poll."""

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_anonymous
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_superuser
        else:
            return False


class UserAnswerPermission(permissions.BasePermission):
    """Определяет доступ для ответов на вопросы пользователей."""

    def has_permission(self, request, view):
        if view.action in ['retrieve', 'create']:
            return request.user.is_anonymous
        else:
            return False


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.filter(end_date__gte=datetime.now())
    permission_classes = [PollAndQuestPermission, ]

    def get_serializer_class(self):
        return PollUpdateSerializer if self.action == 'update' else super().get_serializer_class()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [PollAndQuestPermission, ]


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [PollAndQuestPermission, ]


class UserAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = UserAnswerTextSerializer
    queryset = UserAnswer.objects.all()
    permission_classes = [UserAnswerPermission, ]

    def create(self, request, *args, **kwargs):
        serializer = UserAnswerTextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_answer = serializer.save()

        if request.data.get('choices'):
            request.data['user_answer'] = user_answer.id

            choices = request.data.get('choices')
            for choice in choices:
                request.data['choice'] = choice
                choice_serializer = UserAnswerChoiceSerializer(data=request.data)
                choice_serializer.is_valid(raise_exception=True)
                choice_serializer.save()

        return Response(serializer.data)


class ResultView(ListAPIView):
    serializer_class = PollResultSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = Poll.objects.filter(questions__user_answers__user_id=user_id)
        else:
            queryset = Poll.objects.none()
        return queryset
