from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from subscription.serializers import BirthdaySubscriptionSerializer
from .models import BirthdaySubscription


class BirthdaySubscriptionAPIView(CreateAPIView):
    serializer_class = BirthdaySubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(subscriber=self.request.user)


class BirthdayUnsubscribeAPIView(DestroyAPIView):
    serializer_class = BirthdaySubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        subscribed_to_id = self.kwargs['subscribed_to_id']
        return BirthdaySubscription.objects.get(subscriber=self.request.user, subscribed_to=subscribed_to_id)
