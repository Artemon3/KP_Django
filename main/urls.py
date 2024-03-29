from django.urls import path

from main.apps import MainConfig
from main.views import MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, ClientListView, \
    ClientCreateView, ClientUpdateView, ClientDeleteView, LogsListView, HomeView

app_name = MainConfig.name
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing_edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('mailing_view/<int:pk>', MailingDetailView.as_view(), name='mailing_view'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_add/', MessageCreateView.as_view(), name='message_add'),
    path('message_edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('message_view/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client_add/', ClientCreateView.as_view(), name='client_add'),
    path('client_edit/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('logs_list/', LogsListView.as_view(), name='logs_list'),
]