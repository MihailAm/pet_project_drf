from rest_framework import serializers

from .models import BirthdaySubscription


class BirthdaySubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthdaySubscription
        fields = ('subscribed_to', 'notification_time')
