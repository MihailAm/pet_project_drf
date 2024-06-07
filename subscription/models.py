from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint


class BirthdaySubscription(models.Model):
    subscriber = models.ForeignKey(get_user_model(), related_name='subscriptions', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(get_user_model(), related_name='subscribers', on_delete=models.CASCADE)
    notification_time = models.IntegerField(default=1)  # дни до дня рождения для уведомления

    class Meta:
        constraints = [
            UniqueConstraint(fields=['subscriber', 'subscribed_to'], name='unique_subscription')
        ]
