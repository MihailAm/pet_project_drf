from django.urls import path

from subscription.views import BirthdaySubscriptionAPIView, BirthdayUnsubscribeAPIView

urlpatterns = [
    path('subscribe/', BirthdaySubscriptionAPIView.as_view(), name='subscribe'),
    path('unsubscribe/<int:subscribed_to_id>', BirthdayUnsubscribeAPIView.as_view(), name='unsubscribe')

]
