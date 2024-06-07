from django.core.mail import send_mail
from subscription.models import BirthdaySubscription
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


def send_birthday_notifications():
    today = timezone.now().date()
    subscriptions = BirthdaySubscription.objects.all()

    for subscription in subscriptions:
        birthday = subscription.subscribed_to.date_of_birth
        if birthday:
            notification_date = birthday.replace(year=today.year) - timedelta(days=subscription.notification_time)
            if notification_date == today:
                send_mail(
                    'Напоминание о дне рождения сотрудника',
                    f'Привет {subscription.subscriber.username}. У сотрудника {subscription.subscribed_to.username} день рождение через {subscription.notification_time} дней, не забудь поздравить его.',
                    settings.DEFAULT_FROM_EMAIL,
                    [subscription.subscriber.email],
                    fail_silently=False,
                )
