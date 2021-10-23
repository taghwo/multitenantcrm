from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import permissions
from rest_framework.serializers import Serializer
from .models import Feedback
from modules.ResponseHandler import ResponseHandler
from modules.Paginator import BasePaginator
from .serializer import FeedbackSerializer

class ListCreateFeedback(ListCreateAPIView, ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    pagination_class = BasePaginator

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return self.response_created(serializer.data, 'Feedback submitted')
        except APIException as e:
            return self.response_server_error(e.args)


class RetrieveDeleteFeedback(RetrieveDestroyAPIView, ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return  Feedback.objects.filter(pk=self.kwargs['pk']).first()

    def get(self, request, *args, **kwargs):
        feedback = self.get_queryset()
        if not feedback:
            return self.response_notfound('Feedback')

        serializer =  self.serializer_class(feedback)
        return self.response_ok(serializer.data)

    def delete(self, request, *args, **kwargs):
        feedback = self.get_queryset()

        if not feedback:
              return self.response_notfound('Feedback')

        feedback.delete()

        return self.response_archived('Feedback')